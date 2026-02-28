#Exercício 1 – Converter segundos
segundos = int(input("Entrada: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
seg = resto % 60

print("Saída:", horas, "hora,", minutos, "minuto e", seg, "segundos")


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

print("Maior:", maior)
print("Menor:", menor)


#Exercício 3 – 2 números crescente e decrescente
num1 = int(input("num1: "))
num2 = int(input("num2: "))

if num1 < num2:
    print("Crescente:", num1, ",", num2)
    print("Decrescente:", num2, ",", num1)
else:
    print("Crescente:", num2, ",", num1)
    print("Decrescente:", num1, ",", num2)


#Exercício 4 – Cheque
saldo = float(input("Saldo: "))
cheque = float(input("Cheque: "))

if cheque <= saldo:
    saldo = saldo - cheque
    print("Cheque descontado, saldo:", saldo)
else:
    print("Cheque não pode ser descontado")


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

print("Crescente:", menor, ",", metade, ",", maior)
print("Decrescente:", maior, ",", metade, ",", menor)


#Exercício 6 – Desconto
nome = input("Cliente: ")
compras = float(input("Compras: "))

if compras <= 200:
    descontos = compras * 0.10
elif compras <= 500:
    descontos = compras * 0.15
else:
    descontos = compras * 0.20

total = compras - descontos

print("Nome:", nome)
print("Compras:", compras)
print("Descontos:", descontos)
print("Total para pagar:", total)


#Exercício 7 – Média com pesos
nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))
nota3 = float(input("Nota3: "))

media = (nota1*2 + nota2*3 + nota3*5) / 10

print("Média:", media)

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
print("Média:", media)

contador = 0
for nota in notas:
    if nota >= media:
        contador += 1

print("Notas iguais ou acima da média:", contador)


#Exercício Switch - Exibir Nome do Mês
mes = int(input("Número: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Número nao esta correto")


#Exercício Loop - Identificar Números Pares e Ímpares
pares = 0
impares = 0

for i in range(10):
    numero = int(input("Número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("pares:", pares)
print("impares:", impares)