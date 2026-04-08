# Lab01 - Chat com deteção GDPR

Sistema de chat multi-utilizador em Python. O servidor verifica as mensagens em tempo real e bloqueia as que contiverem dados pessoais (de acordo com o GDPR).

---

## Funcionalidades

- chat em tempo real entre varios utilizadores
- deteção de dados pessoais nas mensagens (email, telefone, IP, nome, data nasc., cartao credito)
- mensagens privadas com @username
- registo de incidentes em JSON
- interface CLI

---

## Estrutura do projeto

```
Lab01/
  config.py                    - constantes (host, porta, etc)
  gdpr_detector.py             - modulo de deteção com regex
  social_engineering_logger.py - guarda incidentes em incidents.json
  server.py                    - servidor TCP com threading
  client.py                    - cliente de chat
  test_stress.py               - teste de stress com 5 clientes
  incidents.json               - criado automaticamente
  README.md
```

---

## Como executar

**Terminal 1 - servidor:**
```
python server.py
```

**Terminal 2 e seguir - clientes:**
```
python client.py
```

Ao ligar pede username. Depois e so escrever mensagens.

- `exit` - desliga
- `@username mensagem` - mensagem privada

---

## Como funciona a deteção GDPR

O modulo `gdpr_detector.py` usa expressoes regulares para encontrar dados pessoais nas mensagens. quando encontra algum o servidor bloqueia a mensagem e manda um aviso ao cliente, O incidente fica guardado em `incidents.json` com o username e o timestamp e o que foi encontrado.

Dados que deteta:

- emails ex: joao@gmail.com
- telefones ex: 912345678, +351 912345678
- enderecos IPv4 ex: 192.168.1.1
- nomes com 2+ palavras ex: João Silva
- datas de nascimento ex: DD/MM/YYYY ou YYYY-MM-DD
- numeros de cartao de credito - validados pelo algoritmo de luhn

Exemplo de mensagem bloqueada:
```
> ola o meu email e joao@gmail.com
[15:32:10] !! [AVISO] Mensagem bloqueada - contem dados pessoais
```

---

## Ficheiro de incidentes

Cada bloqueio fica registado assim em `incidents.json`:

```json
[
  {
    "timestamp": "2026-04-06T15:32:10.123456",
    "username": "joao",
    "original_message": "ola o meu email e joao@gmail.com",
    "detected_data_types": ["email"]
  }
]
```

Para ver os incidentes de um utilizador:

```python
from social_engineering_logger import get_incidents_by_user
incidentes = get_incidents_by_user('joao')
print(incidentes)
```

---

## Teste de stress

Com o servidor a correr em outro terminal:

```
python test_stress.py
```

cria 5 clientes em simultaneo e cada um envia 3 mensagens ex: 1 normal + 2 com dados pessoais e no final aparece um relatorio com quantas foram bloqueadas.

---

## Erros comuns

`Address already in use` — porta 5555 ocupada e ao fechar o outro terminal ou mudar PORT no config.py

`Connection refused` — servidor nao esta a correr tente comecar pelo `python server.py`

---

## Aluno

Jeremias Amado — Lab01 
