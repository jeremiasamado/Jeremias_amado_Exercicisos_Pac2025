# Exercício 1 – 30 primeiros pares e ímpares
def exercicio_1():
    print("os 30 primeiros numeros pares:")
    for par in range(0, 60, 2):
        print(par)

    print("os 30 primeiros numeros impares:")
    for impar in range(1, 60, 2):
        print(impar)


# Exercício 2 – Ver se 10 números são par ou ímpar
def exercicio_2():
    for x in range(10):
        valor = int(input("escreve um numero: "))
        if valor % 2 == 0:
            print(valor, "e par")
        else:
            print(valor, "e ímpar")


# Exercício 3 – Média de 10 alunos
def exercicio_3():
    soma_notas = 0

    for i in range(1, 11):
        texto_pergunta = "diz a nota do aluno " + str(i) + ": "
        nota = float(input(texto_pergunta))
        soma_notas = soma_notas + nota

    media = soma_notas / 10
    print("A media da turma e:", media)


# Exercício 4 – Número primo
def exercicio_4():
    numero = int(input("qual número queres verificar? "))
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1

    if divisores == 2:
        print(numero, "e um numero primo")
    else:
        print(numero, "nao e primo")


# Exercício 5 – Escrever até 10.000
def exercicio_5():
    for numero in range(1, 10001):
        print(numero)


# Exercício 6 – Dez primeiros primos
def exercicio_6():
    quantidade_encontrada = 0
    testar_num = 2 

    print("Os 10 primeiros numeros primos sao:")

    while quantidade_encontrada < 10:
        divisores = 0
        for i in range(1, testar_num + 1):
            if testar_num % i == 0:
                divisores = divisores + 1
                
        if divisores == 2:
            print(testar_num)
            quantidade_encontrada = quantidade_encontrada + 1
            
        testar_num = testar_num + 1


# Exercício 7 – Série de 10 em 10
def exercicio_7():
    for valor in range(10, 1001, 10):
        print(valor)


# Exercício 8 – Duas séries diferentes
def exercicio_8():
    print("serie 1 (10 em 10):")
    for s1 in range(10, 1001, 10):
        print(s1)

    print("\nserie 2 (Começa no 15 e salta 10):")
    for s2 in range(15, 996, 10):
        print(s2)


# Exercício 9 – Validar entrada entre 1 e 100
def exercicio_9():
    while True:
        escolha = int(input("diz um numero entre 1 e 100: "))
        
        if escolha >= 1 and escolha <= 100:
            print("boa! O numero", escolha, "está no intervalo.")
            break
        else:
            print("numero errado. Tenta outra vez.")


# Exercício 10 – Contar divisores
def exercicio_10():
    n_lido = int(input("escreve um numero para ver os divisores: "))
    total_divisores = 0

    for x in range(1, n_lido + 1):
        if n_lido % x == 0:
            total_divisores = total_divisores + 1

    print("O numero", n_lido, "tem", total_divisores, "divisores.")


# Exercício 11 – Desenhar com números
def exercicio_11():
    for linha in range(1, 6):
        texto = str(linha) * linha
        print(texto)

# Exercício 12 - Soma, subtração, divisão e multiplicação
def exercicio_12():
    valor = int(input("diz um numero: "))
    total_operacoes = 0
    
    
    for i in range(1, valor):
        print(valor, "+", i, "=", valor + i)
        print(valor, "-", i, "=", valor - i)
        print(valor, "x", i, "=", valor * i)
        print(valor, "/", i, "=", valor / i)
        
        
        total_operacoes = total_operacoes + 4
        
    print("foram efetuadas", total_operacoes, "operaçoes matematicas.")


#Exercício 13 - ler um número e mostrar a tabuada 1-10
def exercicio_13():
    numero = int(input("numero da tabuada: "))

    for i in range(1,11):
        print(numero,"x",i,"=",numero*i)


# Exercício 14 - Tabuadas do 1 ao 100
def exercicio_14():
    
    for numero in range(1, 101):
        print("--- tabuada do", numero, "---")
        
        
        for i in range(1, 11):
            resultado = numero * i
            print(numero, "x", i, "=", resultado)


#Exercício 15 -  Código ASCII e para de 20 em 20
def exercicio_15():
    conta_linhas = 0
    
    for i in range(256):
        
        print("Código", i, "->", chr(i))
        conta_linhas = conta_linhas + 1
        
        
        if conta_linhas == 20:
            resposta = input("queres continuar? (s/n): ")
            if resposta == "n":
                print("programa terminado.")
                break 
            
            conta_linhas = 0


# Exercício 16 - Média de 30 números pares
def exercicio_16():
    soma_dos_pares = 0
    quantos_pares = 0
    
    while quantos_pares < 30:
        n = int(input("escreve um numero entre 1 e 50: "))
        if n >= 1 and n <= 50:   
            if n % 2 == 0:
                soma_dos_pares = soma_dos_pares + n
                quantos_pares = quantos_pares + 1
                print("boa, faltam", 30 - quantos_pares, "numeros.")
        else:
            print("O número não e valido. Tem de ser entre 1 e 50.")
            
    media_final = soma_dos_pares / 30
    print("a media dos 30 números pares e:", media_final)


# Exercício 17 - Múltiplos de 5, mas não de 3
def exercicio_17():
    print("multiplos de 5 mas nao de 3 (de 1 a 1000):")
    for valor in range(1, 1001):
        if valor % 5 == 0 and valor % 3 != 0:
            print(valor)


# Exercício 18 - Quantos números perfeitos existem
def exercicio_18():
    limite = int(input("ate que numero queres procurar perfeitos? "))
    total_perfeitos = 0
    
    for testar_numero in range(1, limite + 1):
        soma_divisores = 0
        
        for divisor in range(1, testar_numero):
            if testar_numero % divisor == 0:
                soma_divisores = soma_divisores + divisor
                
        if soma_divisores == testar_numero:
            print(testar_numero, "e um numero perfeito.")
            total_perfeitos = total_perfeitos + 1
            
    print("existem", total_perfeitos, "numeros perfeitos.")


# Exercício 19 - Os primeiros 60 números de Fibonacci
def exercicio_19():
    a = 1
    b = 1 
    print(a)
    print(b)
    for i in range(58):
        proximo = a + b
        print(proximo)
        a = b
        b = proximo

    

# teste final - Analise de Números e Calculadora
def teste_final_1():
    while True:
        print("\n--- menu principal ---")
        print("1 - analise de numeros (Primos, Divisores, Perfeitos)")
        print("2 - calculadora e tabuada")
        print("3 - sair")
        opcao = input("escolhe uma opçao: ")

        if opcao == "1":
            valor = 0
            while valor < 1 or valor > 30000:
                valor = int(input("escreve um numero entre 1 e 30000: "))

            conta_paragens = 0
            for i in range(valor, 0, -1):
                divisores = 0
                soma_divisores = 0
                for d in range(1, i):
                    if i % d == 0:
                        divisores = divisores + 1
                        soma_divisores = soma_divisores + d
                divisores_totais = divisores + 1
                if divisores_totais == 2:
                    texto_primo = "sim"
            
                else:
                    texto_primo = "nao"

                if soma_divisores == i and i != 1:
                    texto_perfeito = "sim"
                else:
                    texto_perfeito = "nao"
                    
                print("numero:", i, " | primo:", texto_primo, " | divisores:", divisores_totais, " | perfeito:", texto_perfeito)

                conta_paragens = conta_paragens + 1
                if conta_paragens == 10:
                    parar = input("queres parar? (s/n): ").lower()
                    if parar == "s":
                        break
                    conta_paragens = 0 

        elif opcao == "2":
            print("\n--- calculadora ---")
            print("1 - somar")
            print("2 - subtrair")
            print("3 - multiplicar")
            print("4 - dividir")
            print("5 - tabuada (Função Extra)")
            calc = input("O que queres fazer? ")

            if calc == "5":
                
                v_tabuada = 0
                while v_tabuada < 1 or v_tabuada > 1000:
                    v_tabuada = int(input("tabuada até que numero? (1 a 1000): "))
                
                conta_linhas = 0
                for i in range(1, v_tabuada + 1):
                    print(v_tabuada, "x", i, "=", v_tabuada * i)
                    
                    
                    conta_linhas = conta_linhas + 1
                    if conta_linhas == 20:
                        parar = input("queres parar a tabuada? (s/n): ").lower()
                        if parar == "s":
                            break
                        conta_linhas = 0
            else:
                n1 = float(input("primeiro número: "))
                n2 = float(input("segundo número: "))
                
                if calc == "1": print("resultado:", n1 + n2)
                elif calc == "2": print("resultado:", n1 - n2)
                elif calc == "3": print("resultado:", n1 * n2)
                elif calc == "4": print("resultado:", n1 / n2)
                else: print("operaçao invalida.")

        elif opcao == "3":
            print("a sair do programa...")
            break
        else:
            print("opçao invalida, tenta outra vez.")


# teste final - base de dados de clientes da fabrica
def teste_final_2():
    lista_clientes = []
    numero_automatico = 1

    while True:
        print("\n--- fabrica de materiais ---")
        print("1 - inserir novo cliente")
        print("2 - listar todos os clientes")
        print("3 - procurar cliente por número")
        print("4 - dair")
        escolha = input("opçao: ")

        if escolha == "1":
            nome = input("nome do cliente: ")
            morada = input("morada: ")
            telefone = input("telefone: ")
            nif = input("nif: ")
            valor_compra = float(input("valor da compra: "))

            
            if valor_compra < 100:
                desconto = 0
            elif valor_compra >= 100 and valor_compra <= 200:
                desconto = valor_compra * 0.05
            elif valor_compra > 200 and valor_compra <= 500:
                desconto = valor_compra * 0.10
            else:
                desconto = valor_compra * 0.15

            divida_final = valor_compra - desconto

            
            cliente_novo = {
                "numcli": numero_automatico,
                "nomCli": nome,
                "morada": morada,
                "tel": telefone,
                "nif": nif,
                "compra": valor_compra,
                "divfin": divida_final
            }

            lista_clientes.append(cliente_novo)
            print("cliente gravado com sucesso! O numero dele e o:", numero_automatico)
            
            
            numero_automatico = numero_automatico + 1

        elif escolha == "2":
            if len(lista_clientes) == 0:
                print("ainda nao ha clientes registados.")
            else:
                for cli in lista_clientes:
                    print("\n--- Cliente", cli["Numcli"], "---")
                    print("nome:", cli["NomCli"])
                    print("morada:", cli["morada"])
                    print("telefone:", cli["tel"])
                    print("nif:", cli["nif"])
                    print("valor da Compra:", cli["compra"], "€")
                    print("dívida Final a pagar:", cli["Divfin"], "€")
                    
                    
                    pausa = input("Clica no Enter para ver o próximo, ou escreve 'sair' para parar: ")
                    if pausa.lower() == "sair":
                        break

        elif escolha == "3":
            procurar_num = int(input("qual e o numero do cliente que queres procurar? "))
            encontrou = False

            for cli in lista_clientes:
                if cli["numcli"] == procurar_num:
                    print("encontrado! O cliente e o", cli["NomCli"], "e tem uma dívida de", cli["Divfin"], "€")
                    encontrou = True
                    break
            
            if encontrou == False:
                print("nao existe nenhum cliente com esse numero.")

        elif escolha == "4":
            print("a desligar a base de dados...")
            break
        else:
            print("opcao errada.")