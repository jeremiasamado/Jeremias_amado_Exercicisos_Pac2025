import re

# regex patterns para detetar dados pessoais
# baseado no que o prof pediu no enunciado

EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# telefones - formato portugues e internacional
PHONE_PATTERN = r'(\+351\s?9\d{8}|00351\s?9\d{8}|9\d{8}|\+\d{1,3}\s?\d{6,10})'

# ipv4 tipo 192.168.x.x etc
IP_ADDRESS_PATTERN = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

# nome completo = 2+ palavras que comecam com maiuscula
FULL_NAME_PATTERN = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b'

# datas DD/MM/YYYY ou YYYY-MM-DD
BIRTH_DATE_PATTERN = r'(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})'

# cartao credito 16 digitos (com ou sem espacos entre grupos)
CREDIT_CARD_PATTERN = r'\b(?:\d{4}\s?){3}\d{4}\b|\b\d{16}\b'


def _check_luhn(n):
    # validacao pelo algoritmo de luhn
    # pesquisei como funciona - basicamente multiplica digitos alternados por 2
    if not n.isdigit() or len(n) != 16:
        return False

    nums = [int(x) for x in n]

    for i in range(0, len(nums), 2):
        nums[i] = nums[i] * 2
        if nums[i] > 9:
            nums[i] = nums[i] - 9

    total = sum(nums)
    return total % 10 == 0


def detect_personal_data(msg):
    # percorre a mensagem e retorna um dict com o que encontrou
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

    # para cartoes ainda valida com luhn antes de adicionar
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
    # retorna True se encontrar qualquer dado pessoal
    dados = detect_personal_data(msg)
    return len(dados) > 0
