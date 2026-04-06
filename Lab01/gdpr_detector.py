import re

# regex para detetar dados pessoais

EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# telefones portugueses e internacionais
PHONE_PATTERN = r'(\+351\s?9\d{8}|00351\s?9\d{8}|9\d{8}|\+\d{1,3}\s?\d{6,10})'

# ipv4 basico
IP_ADDRESS_PATTERN = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# nome completo - duas ou mais palavras com maiuscula
FULL_NAME_PATTERN = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b'

# formato DD/MM/YYYY ou YYYY-MM-DD
BIRTH_DATE_PATTERN = r'(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})'

# cartao de credito 16 digitos
CREDIT_CARD_PATTERN = r'\b(?:\d{4}\s?){3}\d{4}\b|\b\d{16}\b'


def _check_luhn(numero):
    # validar cartao com algoritmo de luhn
    if not numero.isdigit() or len(numero) != 16:
        return False

    digits = [int(d) for d in numero]

    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return sum(digits) % 10 == 0


def detect_personal_data(msg):
    encontrado = {}

    emails = re.findall(EMAIL_PATTERN, msg)
    if emails:
        encontrado['email'] = emails

    phones = re.findall(PHONE_PATTERN, msg)
    if phones:
        encontrado['phone'] = phones

    ips = re.findall(IP_ADDRESS_PATTERN, msg)
    if ips:
        encontrado['ip_address'] = ips

    nomes = re.findall(FULL_NAME_PATTERN, msg)
    if nomes:
        encontrado['full_name'] = nomes

    datas = re.findall(BIRTH_DATE_PATTERN, msg)
    if datas:
        encontrado['birth_date'] = datas

    # verificar cartoes com luhn
    cartoes = re.findall(CREDIT_CARD_PATTERN, msg)
    validos = []
    for c in cartoes:
        c_limpo = c.replace(' ', '')
        if _check_luhn(c_limpo):
            validos.append(c)

    if validos:
        encontrado['credit_card'] = validos

    return encontrado


def has_personal_data(msg):
    return bool(detect_personal_data(msg))
