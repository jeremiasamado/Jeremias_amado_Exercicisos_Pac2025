import re as reg
import json
import os


pasta = os.path.dirname(os.path.realpath(__file__))
print("pasta:", repr(pasta))
print("existe?", os.path.exists(pasta))


# Exercício 1 - Ler o ficheiro JSON
f = open(os.path.join(pasta, "dados.json"), "r", encoding="utf-8")
dados = json.load(f)
f.close()

print("Exercício 1 - Conteúdo do ficheiro:")
for registro in dados:
    print(registro)



# Exercício 2 - Validar emails com regex
padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

print("\nExercício 2 - Emails validados:")
for registro in dados:
    email = registro["email"]
    resultado = reg.match(padrao_email, email)
    if resultado:
        print(email + " - válido")
    else:
        print(email + " - inválido")



# Exercício 3 - Extrair domínios dos sites

print("\nExercício 3 - Domínios extraídos:")
for registro in dados:
    site = registro["site"]
    dominio = reg.sub(r"https://|http://|www\.", "", site)
    print(dominio)



# Exercício 4 - Validar NIFs com regex
padrao_nif = r"^[123568]\d{8}$"

print("\nExercício 4 - NIFs validados:")
for registro in dados:
    nif = registro["nif"]
    resultado = reg.match(padrao_nif, nif)
    if resultado:
        print(nif + " - válido")
    else:
        print(nif + " - inválido")



# Exercício 5 - Guardar registos válidos num novo ficheiro JSON
registos_validos = []

for registro in dados:
    email     = registro["email"]
    nif       = registro["nif"]
    telemovel = registro["telemovel"]

    email_valido = reg.match(padrao_email, email)
    nif_valido   = reg.match(padrao_nif, nif)

   
    telemovel_limpo = reg.sub(r"[\s\-]", "", telemovel)
    telemovel_valido = reg.match(r"^\d{9}$", telemovel_limpo)

    if email_valido and nif_valido and telemovel_valido:
        registos_validos.append(registro)

f_validos = open(os.path.join(pasta, "validos.json"), "w", encoding="utf-8")
json.dump(registos_validos, f_validos, indent=2, ensure_ascii=False)
f_validos.close()

print("\nExercício 5 - Registos válidos guardados em 'validos.json':")
for r in registos_validos:
    print(" -", r["nome"])



# Exercício 6 - Criar ficheiro .txt com nome e email
f_txt = open(os.path.join(pasta, "nomes_emails.txt"), "w", encoding="utf-8")

for registro in dados:
    nome  = registro["nome"]
    email = registro["email"]
    f_txt.write(nome + " | " + email + "\n")

f_txt.close()

print("\nExercício 6 - Ficheiro 'nomes_emails.txt' criado")
