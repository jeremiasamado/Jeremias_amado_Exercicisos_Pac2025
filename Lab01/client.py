import socket
import threading
from datetime import datetime

from config import HOST, PORT, BUFFER_SIZE


class ChatClient:

    def __init__(self):
        self.sock = None
        self.conectado = False
        self.username = None

    def start(self):
        self.username = input("Username: ").strip()
        if not self.username:
            self.username = "anonimo"

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.connect((HOST, PORT))
            self.conectado = True
            print(f"ligado a {HOST}:{PORT}")

            # servidor pede username logo ao ligar
            prompt = self.sock.recv(BUFFER_SIZE).decode('utf-8')
            print(prompt, end='')
            self.sock.send(self.username.encode('utf-8'))

            # thread separada so para receber
            t = threading.Thread(target=self.receber, daemon=True)
            t.start()

            self.enviar()

        except ConnectionRefusedError:
            print(f"nao conseguiu ligar - servidor esta a correr?")
        except Exception as e:
            print(f"erro: {e}")
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

                self.sock.send(msg.encode('utf-8'))

        except KeyboardInterrupt:
            self.conectado = False
        except Exception as e:
            print(f"erro ao enviar: {e}")
            self.conectado = False

    def receber(self):
        try:
            while self.conectado:
                dados = self.sock.recv(BUFFER_SIZE).decode('utf-8')

                if not dados:
                    print("\nservidor desligou")
                    self.conectado = False
                    break

                for linha in dados.strip().split('\n'):
                    if linha:
                        self.mostrar(linha)

        except Exception as e:
            if self.conectado:
                print(f"erro ao receber: {e}")
            self.conectado = False

    def mostrar(self, msg):
        hora = datetime.now().strftime('%H:%M:%S')

        # avisos de bloqueio ficam mais destacados
        if 'AVISO' in msg and 'bloqueada' in msg.lower():
            print(f"\n[{hora}] !! {msg}")
        else:
            print(f"\n[{hora}] {msg}")

        print("> ", end='', flush=True)

    def desligar(self):
        self.conectado = False
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
        print("\ndesconectado")


if __name__ == '__main__':
    c = ChatClient()
    c.start()
