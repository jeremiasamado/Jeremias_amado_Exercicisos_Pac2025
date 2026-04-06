import socket
import threading
from datetime import datetime

from config import HOST, PORT, BUFFER_SIZE


class ChatClient:

    def __init__(self):
        self.socket = None
        self.conectado = False
        self.username = None

    def start(self):
        self.username = input("Username: ").strip()
        if not self.username:
            self.username = "anonimo"

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.connect((HOST, PORT))
            self.conectado = True
            print(f"Conectado a {HOST}:{PORT}")

            # receber pedido de username
            resp = self.socket.recv(BUFFER_SIZE).decode('utf-8')
            print(resp, end='')

            self.socket.send(self.username.encode('utf-8'))

            # thread para receber mensagens em background
            t = threading.Thread(target=self.receber, daemon=True)
            t.start()

            # loop de envio fica na main thread
            self.enviar()

        except ConnectionRefusedError:
            print(f"Nao conseguiu ligar a {HOST}:{PORT}")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            self.desligar()

    def enviar(self):
        try:
            while self.conectado:
                msg = input().strip()

                if not msg:
                    continue

                if msg.lower() == 'exit':
                    self.conectado = False
                    break

                self.socket.send(msg.encode('utf-8'))

        except KeyboardInterrupt:
            self.conectado = False
        except Exception as e:
            print(f"Erro ao enviar: {e}")
            self.conectado = False

    def receber(self):
        try:
            while self.conectado:
                dados = self.socket.recv(BUFFER_SIZE).decode('utf-8')

                if not dados:
                    print("\nServidor desligou")
                    self.conectado = False
                    break

                # pode chegar mais do que uma mensagem de uma vez
                for linha in dados.strip().split('\n'):
                    if linha:
                        self.mostrar(linha)

        except Exception as e:
            if self.conectado:
                print(f"Erro ao receber: {e}")
            self.conectado = False

    def mostrar(self, msg):
        hora = datetime.now().strftime('%H:%M:%S')

        if 'AVISO' in msg and 'bloqueada' in msg.lower():
            print(f"\n[{hora}] !! {msg}")
        elif '[SISTEMA]' in msg:
            print(f"\n[{hora}] {msg}")
        elif '[PRIVADO' in msg:
            print(f"\n[{hora}] {msg}")
        else:
            print(f"\n[{hora}] {msg}")

        print("> ", end='', flush=True)

    def desligar(self):
        self.conectado = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
        print("\nDesconectado")


if __name__ == '__main__':
    c = ChatClient()
    c.start()
