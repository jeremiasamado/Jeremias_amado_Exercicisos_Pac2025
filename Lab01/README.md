# Lab01 - Chat com detecao GDPR

Sistema de chat em Python com suporte a varios utilizadores em simultaneo. O servidor deteta dados pessoais nas mensagens e bloqueia as que tiverem informacao sensivel (gdpr).

---

## O que faz

- chat em tempo real com varios clientes ao mesmo tempo
- deteta e bloqueia mensagens com dados pessoais (emails, telefones, IPs, etc)
- mensagens privadas com @username
- guarda os incidentes num ficheiro JSON para analise

---

## Estrutura

```
Lab01/
  config.py                    - host, porta e constantes
  gdpr_detector.py             - detecao de dados pessoais com regex
  social_engineering_logger.py - registo de incidentes em JSON
  server.py                    - servidor TCP multi-cliente
  client.py                    - cliente de chat
  test_stress.py               - teste com 5 clientes em simultaneo
  incidents.json               - criado automaticamente
  README.md
```

---

## Como correr

Python 3.7 ou superior, sem instalar nada extra.

**1. iniciar o servidor (terminal 1):**
```
python server.py
```

**2. iniciar cliente (terminal 2, 3, etc):**
```
python client.py
```

pede username e ja pode enviar mensagens.

comandos disponiveis:
- `exit` para sair
- `@username mensagem` para mensagem privada

---

## Detecao GDPR

o `gdpr_detector.py` usa regex para encontrar:

- emails
- numeros de telefone PT e internacionais
- enderecos IPv4
- nomes proprios (duas ou mais palavras com maiuscula)
- datas de nascimento (DD/MM/YYYY ou YYYY-MM-DD)
- cartoes de credito com 16 digitos (validados pelo algoritmo de Luhn)

quando encontra algum destes dados a mensagem e bloqueada e o cliente recebe um aviso. o incidente fica guardado no ficheiro JSON.

exemplo:
```
> o meu email e joao@gmail.com
[15:32:10] !! [AVISO] Mensagem bloqueada - contem dados pessoais
```

---

## Incidentes

cada bloqueio fica registado em `incidents.json`:

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

para ver incidentes de um user especifico:

```python
from social_engineering_logger import get_incidents_by_user
print(get_incidents_by_user('joao'))
```

---

## Teste de stress

com o servidor a correr:

```
python test_stress.py
```

liga 5 clientes ao mesmo tempo, cada um envia 3 mensagens (1 normal + 2 com dados pessoais) e no final mostra o relatorio de bloqueios.

---

## Erros frequentes

**Address already in use** - ja ha um servidor na porta 5555, fechar o outro terminal ou mudar o PORT no config.py

**Connection refused** - servidor nao esta a correr, fazer primeiro `python server.py`

---

## Aluno

Jeremias Amado - Lab01 
