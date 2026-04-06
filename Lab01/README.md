# Lab01 - Chat com detecao GDPR

Sistema de chat em Python com suporte a varios utilizadores em simultaneo. O servidor deteta dados pessoais nas mensagens e bloqueia as que tiverem informacao errada.

---

## O que faz

- Chat em tempo real com varios clientes ligados ao mesmo servidor
- Deteta e bloqueia mensagens com dados pessoais (emails, telefones, IPs, etc)
- Mensagens privadas com @username
- Guarda os incidentes num ficheiro JSON

---

## Estrutura

```
Lab01/
  config.py                    - host, porta e outras constantes
  gdpr_detector.py             - detecao de dados pessoais com regex
  social_engineering_logger.py - guarda incidentes em JSON
  server.py                    - servidor TCP
  client.py                    - cliente de chat
  test_stress.py               - teste com 5 clientes em simultaneo
  incidents.json               - criado automaticamente quando ha incidentes
  README.md
```

---

## Como correr

Precisa de Python 3.7 ou superior. Nao e necessario instalar nada.

**Terminal 1 - servidor:**
```
python server.py
```

**Terminal 2 (e seguintes) - cliente:**
```
python client.py
```

O cliente pede um username e depois pode comecar a enviar mensagens.

Para sair escrever `exit`.

Para mensagem privada: `@username mensagem`

---

## Detecao de dados pessoais

O modulo `gdpr_detector.py` usa expressoes regulares para detetar:

- Emails
- Numeros de telefone (PT e internacional)
- Enderecos IPv4
- Nomes completos (duas ou mais palavras com maiuscula)
- Datas de nascimento (DD/MM/YYYY ou YYYY-MM-DD)
- Cartoes de credito (16 digitos, validados com algoritmo de Luhn)

Se uma mensagem tiver algum destes dados o servidor bloqueia-a e avisa o cliente. O incidente fica guardado em `incidents.json`.

Exemplo:
```
> o meu email e joao@gmail.com
[15:32:10] !! [AVISO] Mensagem bloqueada - contem dados pessoais
```

---

## Ficheiro de incidentes

Cada vez que uma mensagem e bloqueada fica registada em `incidents.json`:

exemplo: 
```json
[
  {
    "timestamp": "2026-04-06T15:32:10.123456",
    "username": "joao",
    "original_message": "o meu email e joao@gmail.com",
    "detected_data_types": ["email"]
  }
]
```

Para ver incidentes de um utilizador especifico:

```python
from social_engineering_logger import get_incidents_by_user
print(get_incidents_by_user('joao'))
```

---

## Teste de stress

Com o servidor a correr, abrir outro terminal:

```
python test_stress.py
```

Cria 5 clientes em simultaneo, cada um envia 3 mensagens (1 normal + 2 com dados pessoais). No final mostra quantas foram bloqueadas.

---

## Problemas comuns

`Address already in use` - ja ha um servidor a correr, fechar o outro terminal ou mudar a porta em config.py

`Connection refused` - o servidor nao esta a correr, iniciar primeiro com `python server.py`

---

## Autore

- Jeremias Amado Lab01 
