# Exercício 1 – Converter segundos
segundos_totais = int(input("Quantos segundos? "))

h = segundos_totais // 3600
resto_seg = segundos_totais % 3600
m = resto_seg // 60
s = resto_seg % 60

print("saida:", h, "hora,", m, "minuto e", s, "segundos")


# Exercício 2 – Maior e menor
v1 = int(input("diz o primeiro: "))
v2 = int(input("diz o segundo: "))
v3 = int(input("diz o terceiro: "))

o_maior = v1
o_menor = v1

if v2 > o_maior:
    o_maior = v2
if v3 > o_maior:
    o_maior = v3

if v2 < o_menor:
    o_menor = v2
if v3 < o_menor:
    o_menor = v3

print("maior:", o_maior)
print("menor:", o_menor)


# Exercício 3 – 2 números crescente e decrescente
n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))

if n1 < n2:
    print("crescente:", n1, ",", n2)
    print("decrescente:", n2, ",", n1)
else:
    print("crescente:", n2, ",", n1)
    print("decrescente:", n1, ",", n2)


# Exercício 4 – Cheque
dinheiro_na_conta = float(input("Quanto dinheiro tens? "))
valor_cheque = float(input("Valor do cheque: "))

if valor_cheque <= dinheiro_na_conta:
    dinheiro_na_conta = dinheiro_na_conta - valor_cheque
    print("cheque descontado, saldo:", dinheiro_na_conta)
else:
    print("cheque não pode ser descontado")


# Exercício 5 – 3 valores em ordem
a = int(input("valor a: "))
b = int(input("valor b: "))
c = int(input("valor c: "))

if a <= b and a <= c:
    baixo = a
    if b <= c:
        meio = b
        alto = c
    else:
        meio = c
        alto = b
elif b <= a and b <= c:
    baixo = b
    if a <= c:
        meio = a
        alto = c
    else:
        meio = c
        alto = a
else:
    baixo = c
    if a <= b:
        meio = a
        alto = b
    else:
        meio = b
        alto = a

print("crescente:", baixo, ",", meio, ",", alto)
print("decrescente:", alto, ",", meio, ",", baixo)


# Exercício 6 – Desconto
n_cliente = input("nome do cliente: ")
preço_compra = float(input("valor das compras: "))

if preço_compra <= 200:
    desc = preço_compra * 0.10
elif preço_compra <= 500:
    desc = preço_compra * 0.15
else:
    desc = preço_compra * 0.20

pago_final = preço_compra - desc

print("nome:", n_cliente)
print("compras:", preço_compra)
print("descontos:", desc)
print("total para pagar:", pago_final)


# Exercício 7 – Média com pesos
p1 = float(input("nota da primeira prova: "))
p2 = float(input("nota da segunda prova: "))
p3 = float(input("nota da terceira prova: "))

media_aluno = (p1*2 + p2*3 + p3*5) / 10

print("media:", media_aluno)

if media_aluno >= 6:
    print("APROVADO")
else:
    print("REPROVADO")


# Exercício 8 – Média de 10 notas
total_soma = 0
guardar_notas = []

for x in range(10):
    nota_lida = float(input("Diz a nota: "))
    guardar_notas.append(nota_lida)
    total_soma += nota_lida

m_final = total_soma / 10
print("media das notas:", m_final)

quantos_acima = 0
for n in guardar_notas:
    if n >= m_final:
        quantos_acima = quantos_acima + 1

print("notas iguais ou acima da média:", quantos_acima)


# Exercício Switch - Nome do Mês
mês_escolhido = int(input("Escreve o numero do mes: "))

if mês_escolhido == 1: print("janeiro")
elif mês_escolhido == 2: print("fevereiro")
elif mês_escolhido == 3: print("março")
elif mês_escolhido == 4: print("abril")
elif mês_escolhido == 5: print("maio")
elif mês_escolhido == 6: print("junho")
elif mês_escolhido == 7: print("julho")
elif mês_escolhido == 8: print("agosto")
elif mês_escolhido == 9: print("setembro")
elif mês_escolhido == 10: print("outubro")
elif mês_escolhido == 11: print("novembro")
elif mês_escolhido == 12: print("dezembro")
else: print("Invalido")


# Exercício Loop - Pares e Ímpares
p = 0
i = 0

for contador in range(10):
    val = int(input("escreve um numero: "))
    if val % 2 == 0:
        p += 1
    else:
        i = i + 1

print("pares:", p)
print("impares:", i)