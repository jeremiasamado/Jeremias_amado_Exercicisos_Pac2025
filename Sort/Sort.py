# Exercicio 1: Ordenar palavras por ordem alfabética 
palavras = ["banana", "uva", "abacaxi", "laranja"]

print("Lista original:", palavras)
houve_troca = True
while houve_troca:
    houve_troca = False
    for i in range(len(palavras) - 1):

        p1 = palavras[i]
        p2 = palavras[i + 1]
        deve_trocar = False
        decidido = False
        
        for j in range(min(len(p1), len(p2))):
            if ord(p1[j]) > ord(p2[j]):
                deve_trocar = True
                decidido = True
                break
            elif ord(p1[j]) < ord(p2[j]):
                decidido = True
                break
        if not decidido and len(p1) > len(p2):
            deve_trocar = True
        if deve_trocar:
            palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
            houve_troca = True
print("Lista ordenada A-Z:", palavras)



# Exercicio 2: Ordenar por ordem alfabética inversa
nomes = ["Python", "inteligência", "Aprender", "dados", "Rede"]

print("\nLista original:", nomes)
houve_troca = True
while houve_troca:
    houve_troca = False
    for i in range(len(nomes) - 1):
        p1 = nomes[i].lower()
        p2 = nomes[i + 1].lower()
        deve_trocar = False
        decidido = False

        for j in range(min(len(p1), len(p2))):
            if ord(p1[j]) < ord(p2[j]):
                
                deve_trocar = True
                decidido = True
                break
            elif ord(p1[j]) > ord(p2[j]):
                decidido = True
                break

        if not decidido and len(p1) < len(p2):
            deve_trocar = True

        if deve_trocar:
            nomes[i], nomes[i + 1] = nomes[i + 1], nomes[i]
            houve_troca = True
print("Lista ordenada Z-A:", nomes)



# Exercicio 3: Ordenar os caracteres de uma palavra por ordem alfabética
palavra = "algoritmo"

print("\nPalavra original:", palavra)
letras = []
for c in palavra:
    letras.append(c)
houve_troca = True
while houve_troca:
    houve_troca = False
    for i in range(len(letras) - 1):
        if ord(letras[i]) > ord(letras[i + 1]):
            letras[i], letras[i + 1] = letras[i + 1], letras[i]
            houve_troca = True
resultado = ""
for c in letras:
    resultado = resultado + c
print("Palavra ordenada:", resultado)



# Exercicio 4: Ordenar palavras pela quantidade de letras minusculas
lista4 = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

print("\nLista original:", lista4)

def contar_minusculas(p):
    conta = 0
    for c in p:

        if ord('a') <= ord(c) <= ord('z'):
            conta = conta + 1
    return conta
houve_troca = True
while houve_troca:
    houve_troca = False
    for i in range(len(lista4) - 1):
        if contar_minusculas(lista4[i]) > contar_minusculas(lista4[i + 1]):
            lista4[i], lista4[i + 1] = lista4[i + 1], lista4[i]
            houve_troca = True

print("Lista ordenada por minusculas:", lista4)



# Exercicio 5: Agrupar palavras pela letra inicial e ordenar cada grupo
lista5 = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

print("\nLista original:", lista5)


grupos = {}

for palavra in lista5:
    letra = palavra[0]
    if letra not in grupos:
        grupos[letra] = []
    grupos[letra].append(palavra)
for letra in grupos:
    grupo = grupos[letra]
    houve_troca = True

    while houve_troca:
        houve_troca = False
        for i in range(len(grupo) - 1):

            p1 = grupo[i]
            p2 = grupo[i + 1]
            deve_trocar = False
            decidido = False

            for j in range(min(len(p1), len(p2))):
                if ord(p1[j]) > ord(p2[j]):
                    deve_trocar = True
                    decidido = True
                    break
                elif ord(p1[j]) < ord(p2[j]):
                    decidido = True
                    break

            if not decidido and len(p1) > len(p2):
                deve_trocar = True

            if deve_trocar:
                grupo[i], grupo[i + 1] = grupo[i + 1], grupo[i]
                houve_troca = True

print("Grupos ordenados:", grupos)
