import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9999

serverSocket.bind((host, port))
serverSocket.listen(1)

print(f"server iniciou em {host}: {port}")
print("a espera do cliente...")

clientSocket, addr = serverSocket.accept()
print(f"cliente entrou {addr}")
print("podes escrever uma mensagem para o cliente ou terminar a conversa.\n")

while True:

    mensagem = clientSocket.recv(1024).decode()
    if mensagem.lower() == "sair":
        print("o cliente saiu da ligacao")
        break

    print(f"cliente respondeu: {mensagem}")

    resposta = input("a minha resposta: ")
    clientSocket.send(resposta.encode())

    if resposta.lower() == "sair":
        print("a sair...")
        break

clientSocket.close()
serverSocket.close()
print("a ligacao encerrou")