# exeercício 1 - criar um dicionario
alunos = {}
menu_active = True

while menu_active:
    print("\n--- menu alunos ---")
    print("1 - inserir aluno")
    print("2 - listar alunos")
    print("3 - sair")
    
    opcao = input("escolhe uma: ")
    
    if opcao == "1":
        x = input("id do aluno: ")
        nome = input("nome: ")
        idadee = input("idade: ")
        curso = input("curso: ")
        
        alunos[x] = {'nome': nome, 'idade': idadee, 'curso': curso}
        print("aluno adicionado! ")
        
    elif opcao == "2":
        if len(alunos) == 0:
            print("nenhum aluno registado")
        else:
            for id_al, info in alunos.items():
                print(f"\nnome: {info['nome']}")
                print(f"idade: {info['idade']}")
                print(f"curso: {info['curso']}")
    
    elif opcao == "3":
        menu_active = False
        print("bye!")


# exercício 2 - aceder ao modelo do carro
print("\n\n--- modelos de carros ---")
carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}
print(carro['marca'])
modelo = carro['modelo']
print(modelo)


# exeercício 3
print("\n--- criar e modificar dicionario ---")
produto = {}

produto['nome'] = "Telemóvel"
produto['preço'] = 1500
produto['stock'] = 30

print("antes:")
print(produto)

del produto['stock']
print("\ndepois:")
print(produto)


# exercício 4 - verificar chave
print("\n--- verificar chave ---")
u = {'nome': 'Carlos', 'idade': 28}

if 'email' in u:
    print("email encontrado")
else:
    print("email não encontrado.")


# exercício 5
print("\n--- contar letras numa palavra ---")
p = input("coloca uma palavra: ")

cnt = {}
for l in p:
    if l in cnt:
        cnt[l] += 1
    else:
        cnt[l] = 1

print("resultado: " + str(cnt))


# exeercício 6 - somar
print("\n--- somar valores de vendas ---")
vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}

total = 0
for m in vendas:
    total = total + vendas[m]

print(f"total: {total}")


# exercício 7 - inverter
print("\n--- chaves e valores ---")
d = {'a': 1, 'b': 2, 'c': 3}
inv = {}

for k, vv in d.items():
    inv[vv] = k

print("original: " + str(d))
print("invertido: " + str(inv))


# exeercício 8 - juntar dicts
print("\n--- juntar diccionários ---")
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

result = d1.copy()
result.update(d2)

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"junto: {result}")


# exercício 9 - média
print("\n--- média de notas ---")
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for student in notas:
    s = sum(notas[student])
    m = s / len(notas[student])
    print(f"{student}: {m}")


# exeercício 10 - contar
print("\n--- contar palavras ---")
frase = input("mete uma frase: ")

c = {}
ps = frase.split()

for p in ps:
    if p in c:
        c[p] += 1
    else:
        c[p] = 1

print(f"resultado: {c}")