import re

# padroes para detetar dados pessoais nas mensagens

EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# numeros pt e tambem internacionais com +
PHONE_PATTERN = r'(\+351\s?9\d{8}|00351\s?9\d{8}|9\d{8}|\+\d{1,3}\s?\d{6,10})'

IP_ADDRESS_PATTERN = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# duas ou mais palavras com letra grande = nome proprio
FULL_NAME_PATTERN = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b'

BIRTH_DATE_PATTERN = r'(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})'

# 16 digitos com ou sem espacos
CREDIT_CARD_PATTERN = r'\b(?:\d{4}\s?){3}\d{4}\b|\b\d{16}\b'


def _check_luhn(n):
    # algoritmo de luhn para validar cartao
    if not n.isdigit() or len(n) != 16:
        return False

    nums = [int(x) for x in n]

    # multiplicar posicoes pares por 2
    for i in range(0, len(nums), 2):
        nums[i] *= 2
        if nums[i] > 9:
            nums[i] -= 9

    return sum(nums) % 10 == 0


def detect_personal_data(msg):
    resultado = {}

    emails = re.findall(EMAIL_PATTERN, msg)
    if emails:
        resultado['email'] = emails

    tels = re.findall(PHONE_PATTERN, msg)
    if tels:
        resultado['phone'] = tels

    ips = re.findall(IP_ADDRESS_PATTERN, msg)
    if ips:
        resultado['ip_address'] = ips

    nomes = re.findall(FULL_NAME_PATTERN, msg)
    if nomes:
        resultado['full_name'] = nomes

    datas = re.findall(BIRTH_DATE_PATTERN, msg)
    if datas:
        resultado['birth_date'] = datas

    cartoes = re.findall(CREDIT_CARD_PATTERN, msg)
    validos = []
    for c in cartoes:
        sem_espacos = c.replace(' ', '')
        if _check_luhn(sem_espacos):
            validos.append(c)
    if validos:
        resultado['credit_card'] = validos

    return resultado


def has_personal_data(msg):
    return bool(detect_personal_data(msg))
