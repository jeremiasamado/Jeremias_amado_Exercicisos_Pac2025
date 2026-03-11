# Exercicio 1 - Tipo de dia
dia_semana = input("Qual é o dia? ").lower()

match dia_semana:
    case "sabado" | "domingo":
        print("fim de semana")
    case "segunda" | "terca" | "quarta" | "quinta" | "sexta":
        print("dia útil")
    case _:
        print("dia inválido")


# Exercicio 2 - Classificação de nota
pontos = int(input("Nota de 0 a 100: "))

match pontos:
    case p if p >= 90:
        print("excelente")
    case p if p >= 70:
        print("bom")
    case p if p >= 50:
        print("suficiente")
    case _:
        print("insuficiente")

    
# Exercicio 3 - Tipo de pedido
t = input("tipo (compra/venda): ").lower()
v = float(input("valor em euros: "))

encomenda = {"tipo": t, "valor": v}

match encomenda:
    case {"tipo": "compra", "valor": guito}:
        print("compra de", guito, "€")
    case {"tipo": "venda", "valor": guito}:
        print("venda de", guito, "€")
    case _:
        print("pedido desconhecido")


# Exercicio 4 - Tipo de dado
dado = input("escreve qualquer coisa: ")

if dado.isdigit():
    print("string numérica")
else:
    print("string textual")


# Exercicio 5 - Análise de mensagem
texto_msg = input("escreve a mensagem: ").lower()

match texto_msg:
    case "ola" | "bom dia":
        print("saudação")
    case _ if texto_msg.endswith("?"):
        print("pergunta")
    case _ if "tchau" in texto_msg or "adeus" in texto_msg:
        print("despedida")
    case _:
        print("mensagem genérica")


# Exercicio 6 - Estado do servidor
# Corrigido: Agora o "lento" vem primeiro que o "ok" genérico
situação = input("status do server: ").lower()
tempo_ms = int(input("ms de resposta: "))

info_servidor = {"status": situação, "tempo_resposta": tempo_ms}

match info_servidor:
    case {"status": "ok", "tempo_resposta": tempo} if tempo > 200:
        print("servidor lento")
    case {"status": "ok"}:
        print("servidor ativo")
    case {"status": "erro"}:
        print("servidor indisponível")
    case _:
        print("estado desconhecido")


# Exercicio 7 - Classificação de produto
qual_categoria = input("Categoria: ").lower()
quanto_custa = float(input("Preço: "))

item = {"categoria": qual_categoria, "preco": quanto_custa}

match item:
    case {"categoria": "eletronico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletronico"}:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")


# Exercicio 8 - Operação matemática
fazer_o_que = input("queres somar, subtrair, multiplicar ou dividir? ").lower()
numero1 = float(input("numero 1: "))
numero2 = float(input("numero 2: "))

match fazer_o_que:
    case "soma":
        print(numero1 + numero2)
    case "subtrai":
        print(numero1 - numero2)
    case "multiplica":
        print(numero1 * numero2)
    case "divide":
        print(numero1 / numero2)
    case _:
        print("operação inválida")


# Exercicio 9 - Processamento de requisição
tipo_metodo = input("Metodo (GET/POST): ").upper()
oq_tem_dentro = input("Conteudo: ")

requisicao = {"metodo": tipo_metodo, "conteudo": oq_tem_dentro}

match requisicao:
    case {"metodo": "GET"}:
        print("requisição GET recebida")
    case {"metodo": "POST", "conteudo": ""} | {"metodo": "POST", "conteudo": None}:
        print("requisição POST sem dados")
    case {"metodo": "POST"}:
        print("requisição POST com dados válidos")
    case _:
        print("metodo não suportado")


# Exercicio 10 - Pedra, Papel ou Tesoura
j1 = input("jogador 1: ").lower()
j2 = input("jogador 2: ").lower()

if j1 == j2:
    print("empate")
else:
    match (j1, j2):
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            print("jogador 1 ganhou")
        case _:
            print("jogador 2 ganhou")