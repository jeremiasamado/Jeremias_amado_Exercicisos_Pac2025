#Exercício 1 – Tipo de dia
dia = input("dia da semana: ").lower()

match dia:
    case "sabado" | "domingo":
        print("fim de semana")
    case "segunda" | "terca" | "quarta" | "quinta" | "sexta":
        print("dia útil")
    case _:
        print("dia inválido")


#Exercício 2 – Classificação de nota
nota = int(input("nota (0-100): "))

match nota:
    case n if n >= 90:
        print("excelente")
    case n if 70 <= n <= 89:
        print("bom")
    case n if 50 <= n <= 69:
        print("suficiente")
    case _:
        print("insuficiente")

    
#Exercício 3 – Tipo de pedido
tipo = input("tipo: ").lower()
valor = float(input("Valor: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido:
    case {"tipo": "compra", "valor": v}:
        print("compra de", v, "€")
    case {"tipo": "venda", "valor": v}:
        print("venda de", v, "€")
    case _:
        print("pedido desconhecido")


#Exercício 4 – Tipo de dado
valor = input("valor: ")

match valor:
    case _ if valor.isdigit():
        print("string numérica")
    case _:
        print("string textual")


#Exercício 5 – Análise de mensagem
mensagem = input("mensagem: ").lower()

match mensagem:
    case "olá" | "bom dia":
        print("saudação")
    case m if m.endswith("?"):
        print("pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("despedida")
    case _:
        print("mensagem genérica")


#Exercício 6 – Estado do servidor
status = input("status: ").lower()
tempo = int(input("tempo de resposta (ms): "))

servidor = {"status": status, "tempo_resposta": tempo}

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("servidor lento")
    case {"status": "ok"}:
        print("servidor ativo")
    case {"status": "erro"}:
        print("servidor indisponível")
    case _:
        print("estado desconhecido")


#Exercício 7 – Classificação de produto
categoria = input("Categoria: ").lower()
preco = float(input("Preço: "))

produto = {"categoria": categoria, "preco": preco}

match produto:
    case {"categoria": "eletronico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletronico", "preco": p}:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")


#Exercício 8 – Operação matemática
operacao = input("operação: ").lower()
n1 = float(input("número 1: "))
n2 = float(input("número 2: "))

match operacao:
    case "soma":
        print(n1 + n2)
    case "subtrai":
        print(n1 - n2)
    case "multiplica":
        print(n1 * n2)
    case "divide":
        print(n1 / n2)
    case _:
        print("operação inválida")


#Exercício 9 – Processamento de requisição
metodo = input("metodo: ").upper()
conteudo = input("Conteudo: ")

req = {"metodo": metodo, "conteudo": conteudo}

match req:
    case {"metodo": "GET"}:
        print("requisição GET recebida")
    case {"metodo": "POST", "conteudo": ""}:
        print("requisição POST sem dados")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("requisição POST com dados válidos")
    case _:
        print("método não suportado")


#Exercício 10 – Pedra, Papel ou Tesoura
j1 = input("jogador 1: ").lower()
j2 = input("jogador 2: ").lower()

match (j1, j2):
    case (a, b) if a == b:
        print("empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("jogador 1 venceu")
    case _:
        print("jogador 2 venceu")