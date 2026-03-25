import re as reg
import datetime

# exercício 1 - ler ficheiro dados.txt
f = open("dados.txt", "r", encoding="utf-8")
conteudo = f.read()
f.close()

print("conteúdo do ficheiro:")
print(conteudo)


# exercício 2 - encontrar emails
emails = reg.findall(r"Email:\s*([\w\.-]+@[\w\.-]+)", conteudo)

print("\nemails encontrados:")
for email in emails:
    print(email)


# exercício 3 - encontrar telemóveis
telemoves = reg.findall(r"Telemóvel:\s*(\d[\d \-]+\d|\d{9})", conteudo)

print("\ntelemoveis encontrados:")
for telem in telemoves:
    print(telem)


# exercício 4 - extrair nomes
nomes = reg.findall(r"Nome:\s*([\w\u00C0-\u00FF\s]+),", conteudo)

print("\nnomes encontrados:")
for nome in nomes:
    print(nome.strip())


# exercício 5 - criar ficheiro extraidos.txt
f_extraidos = open("extraidos.txt", "w", encoding="utf-8")

for i in range(len(nomes)):
    nome_limpo = nomes[i].strip()
    email = emails[i]
    telem = telemoves[i]

    f_extraidos.write(nome_limpo + " | " + email + " | " + telem + "\n")

f_extraidos.close()

print("\nficheiro 'extraidos.txt' criado")


# exercício 6 - emails que terminam em .pt
emails_pt = reg.findall(r"([\w\.-]+@[\w\.-]+\.pt)", conteudo)

print("\nemails com terminação .pt:")
for email in emails_pt:
    print(email)


f_registos = open("registos.txt", "r", encoding="utf-8")
conteudo_registos = f_registos.read()
f_registos.close()


# exercício 7 - extrair NIFs
nifs = reg.findall(r"NIF:\s*(\d{9})", conteudo_registos)

print("\nnifs encontrados:")
for nif in nifs:
    print(nif)


# exercício 8 - extrair datas
datas = reg.findall(r"Data:\s*(\d{2}/\d{2}/\d{4})", conteudo_registos)

print("\ndatas encontradas:")
for data in datas:
    print(data)


# exercício 9 - extrair códigos postais
codigos = reg.findall(r"Código Postal:\s*(\d{4}-\d{3})", conteudo_registos)

print("\ncódigos postais encontrados:")
for codigo in codigos:
    print(codigo)


# exercício 10 - extrair domínios dos sites
dominios_raw = reg.findall(r"Site:\s*(.+)", conteudo_registos)

print("\ndomínios encontrados:")
for dominio in dominios_raw:
    dominio_limpo = reg.sub(r"https://|http://|www\.", "", dominio)
    print(dominio_limpo)


# exercício 11 - validar NIFs que começam com dígito válido
nifs_validos = reg.findall(r"NIF:\s*([123568]\d{8})", conteudo_registos)

print("\nnifs corretos (começam com 1,2,3,5,6,8):")
for nif in nifs_validos:
    print(nif)


# exercício 12 - criar ficheiro resumo.txt
nomes_reg = reg.findall(r"Nome:\s*([\w\u00C0-\u00FF\s]+)\s*\|", conteudo_registos)
nifs_reg = reg.findall(r"NIF:\s*(\d{9})", conteudo_registos)
datas_reg = reg.findall(r"Data:\s*(\d{2}/\d{2}/\d{4})", conteudo_registos)
codigos_reg = reg.findall(r"Código Postal:\s*(\d{4}-\d{3})", conteudo_registos)
dominios_reg = reg.findall(r"Site:\s*(.+)", conteudo_registos)

f_resumo = open("resumo.txt", "w", encoding="utf-8")

for i in range(len(nomes_reg)):
    nome = nomes_reg[i].strip()
    nif = nifs_reg[i]
    data = datas_reg[i]
    codigo = codigos_reg[i]
    dominio = reg.sub(r"https://|http://|www\.", "", dominios_reg[i])

    f_resumo.write(nome + " | " + nif + " | " + data + " | " + codigo + " | " + dominio + "\n")

f_resumo.close()

print("\nficheiro 'resumo.txt' criado")


# exercício 13 - registos com datas anteriores a 2025
print("\nregistos com datas anteriores a 2025:")

data_limite = datetime.date(2025, 1, 1)

linhas = conteudo_registos.split("\n")

for linha in linhas:
    data_match = reg.search(r"Data:\s*(\d{2})/(\d{2})/(\d{4})", linha)

    if data_match:
        dia = int(data_match.group(1))
        mes = int(data_match.group(2))
        ano = int(data_match.group(3))

        data_registo = datetime.date(ano, mes, dia)

        if data_registo < data_limite:
            nome_match = reg.search(r"Nome:\s*([\w\u00C0-\u00FF\s]+)\s*\|", linha)
            if nome_match:
                nome = nome_match.group(1).strip()
                print(nome + " - Data: " + data_match.group(1) + "/" + data_match.group(2) + "/" + data_match.group(3))