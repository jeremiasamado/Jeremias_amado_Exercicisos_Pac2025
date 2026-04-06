import socket
import threading
import time

from config import HOST, PORT, BUFFER_SIZE


class ClienteTeste(threading.Thread):

    def __init__(self, cid):
        super().__init__(daemon=True)
        self.cid = cid
        self.username = f"teste_{cid}"
        self.socket = None
        self.bloqueadas = 0
        self.enviadas = 0

    def run(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((HOST, PORT))
            self.socket.settimeout(3)

            print(f"[cliente {self.cid}] conectado")

            self.socket.recv(BUFFER_SIZE)  # prompt username
            self.socket.send(self.username.encode('utf-8'))
            self.socket.recv(BUFFER_SIZE)  # boas vindas

            # mensagem normal
            self.mandar("Ola a todos")

            # email - deve ser bloqueado
            self.mandar(f"o meu email e teste{self.cid}@mail.com")

            # telefone - deve ser bloqueado
            self.mandar("liguem para 912345678")

            time.sleep(2)
            self.ler_respostas()
            self.socket.close()

            print(f"[cliente {self.cid}] fim - enviadas:{self.enviadas} bloqueadas:{self.bloqueadas}")

        except Exception as e:
            print(f"[cliente {self.cid}] erro: {e}")

    def mandar(self, msg):
        try:
            self.socket.send(msg.encode('utf-8'))
            self.enviadas += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"[cliente {self.cid}] erro envio: {e}")

    def ler_respostas(self):
        try:
            while True:
                dados = self.socket.recv(BUFFER_SIZE).decode('utf-8')
                if not dados:
                    break
                if 'AVISO' in dados and 'bloqueada' in dados.lower():
                    self.bloqueadas += 1
        except socket.timeout:
            pass
        except Exception:
            pass


def correr_teste(n=5):
    print(f"\n{'='*50}")
    print(f"STRESS TEST - {n} clientes")
    print(f"Servidor: {HOST}:{PORT}")
    print(f"{'='*50}\n")

    clientes = []
    for i in range(n):
        c = ClienteTeste(i)
        clientes.append(c)
        c.start()
        time.sleep(0.5)

    for c in clientes:
        c.join()

    total_bloq = sum(c.bloqueadas for c in clientes)
    total_env = sum(c.enviadas for c in clientes)

    print(f"\n{'='*50}")
    print("RESULTADO FINAL")
    print(f"{'='*50}")
    for c in clientes:
        print(f"cliente {c.cid}: enviadas={c.enviadas} bloqueadas={c.bloqueadas}")

    print(f"\nTotal enviadas: {total_env}")
    print(f"Total bloqueadas: {total_bloq}")
    if total_env > 0:
        print(f"Taxa de bloqueio: {total_bloq/total_env*100:.1f}%")
    print(f"{'='*50}\n")


if __name__ == '__main__':
    input(f"Servidor em {HOST}:{PORT}? Prima ENTER para comecar...")
    correr_teste(5)
