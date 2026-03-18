import socket


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9999

clientSocket.connect((host, port))

print("ligado ao server com sucesso")
print("podes escrever uma mensagem para o server")

while True:
    mensagem = input("eu:")
    clientSocket.send(mensagem.encode())

    if mensagem.lower() == "sair":
        print("a terminar a ligacao com o server")
        break

    resposta = clientSocket.recv(1024).decode()

    if resposta.lower() == "sair":
        print("o servidor terminou a ligacao")
        break

    print(f"server respondeu: {resposta}")

clientSocket.close()
print("a ligaçao com o server encerrou")