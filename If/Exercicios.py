#Exercício 1 – Converter segundos
segundos = int(input("entrada: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
seg = resto % 60

print("saida:", horas, "hora,", minutos, "minuto e", seg, "segundos")


#Exercício 2 – Maior e menor
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("maior:", maior)
print("menor:", menor)


#Exercício 3 – 2 números crescente e decrescente
num1 = int(input("num1: "))
num2 = int(input("num2: "))

if num1 < num2:
    print("crescente:", num1, ",", num2)
    print("decrescente:", num2, ",", num1)
else:
    print("crescente:", num2, ",", num1)
    print("decrescente:", num1, ",", num2)


#Exercício 4 – Cheque
saldo = float(input("saldo: "))
cheque = float(input("cheque: "))

if cheque <= saldo:
    saldo = saldo - cheque
    print("cheque descontado, saldo:", saldo)
else:
    print("cheque não pode ser descontado")


#Exercício 5 – 3 valores em ordem
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        metade = num2
        maior = num3
    else:
        metade = num3
        maior = num2

elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        metade = num1
        maior = num3
    else:
        metade = num3
        maior = num1

else:
    menor = num3
    if num1 <= num2:
        metade = num1
        maior = num2
    else:
        metade = num2
        maior = num1

print("crescente:", menor, ",", metade, ",", maior)
print("decrescente:", maior, ",", metade, ",", menor)


#Exercício 6 – Desconto
nome = input("cliente: ")
compras = float(input("compras: "))

if compras <= 200:
    descontos = compras * 0.10
elif compras <= 500:
    descontos = compras * 0.15
else:
    descontos = compras * 0.20

total = compras - descontos

print("nome:", nome)
print("compras:", compras)
print("descontos:", descontos)
print("total para pagar:", total)


#Exercício 7 – Média com pesos
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))

media = (nota1*2 + nota2*3 + nota3*5) / 10

print("media:", media)

if media >= 6:
    print("peso normal")
else:
    print("acima do peso normal")


#Exercício 8 – Média de 10 notas
soma = 0
notas = []

for i in range(10):
    nota = float(input("Nota: "))
    notas.append(nota)
    soma += nota

media = soma / 10
print("media:", media)

contador = 0
for nota in notas:
    if nota >= media:
        contador += 1

print("notas iguais ou acima da média:", contador)


#Exercício Switch - Exibir Nome do Mês
mes = int(input("numero: "))

if mes == 1:
    print("janeiro")
elif mes == 2:
    print("fevereiro")
elif mes == 3:
    print("março")
elif mes == 4:
    print("abril")
elif mes == 5:
    print("maio")
elif mes == 6:
    print("junho")
elif mes == 7:
    print("julho")
elif mes == 8:
    print("agosto")
elif mes == 9:
    print("setembro")
elif mes == 10:
    print("outubro")
elif mes == 11:
    print("novembro")
elif mes == 12:
    print("dezembro")
else:
    print("numero nao esta correto")


#Exercício Loop - Identificar Números Pares e Ímpares
pares = 0
impares = 0

for i in range(10):
    numero = int(input("numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("pares:", pares)
print("impares:", impares)