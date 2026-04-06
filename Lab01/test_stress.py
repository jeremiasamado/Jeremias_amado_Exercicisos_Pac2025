import socket
import threading
import time

from config import HOST, PORT, BUFFER_SIZE


class ClienteTeste(threading.Thread):

    def __init__(self, cid):
        super().__init__(daemon=True)
        self.cid = cid
        self.username = f"teste_{cid}"
        self.sock = None
        self.bloqueadas = 0
        self.enviadas = 0

    def run(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            self.sock.settimeout(3)

            print(f"[{self.cid}] conectado")

            self.sock.recv(BUFFER_SIZE)  # prompt do username
            self.sock.send(self.username.encode('utf-8'))
            self.sock.recv(BUFFER_SIZE)  # mensagem de boas vindas

            # mensagem normal - nao deve ser bloqueada
            self.mandar("ola a todos")

            # com email - deve ser bloqueada
            self.mandar(f"email: teste{self.cid}@mail.com")

            # com telefone - deve ser bloqueada
            self.mandar("tel: 912345678")

            time.sleep(2)
            self.ler_respostas()
            self.sock.close()

            print(f"[{self.cid}] terminado - ok:{self.enviadas - self.bloqueadas} bloq:{self.bloqueadas}")

        except Exception as e:
            print(f"[{self.cid}] erro: {e}")

    def mandar(self, msg):
        try:
            self.sock.send(msg.encode('utf-8'))
            self.enviadas += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"[{self.cid}] erro envio: {e}")

    def ler_respostas(self):
        try:
            while True:
                dados = self.sock.recv(BUFFER_SIZE).decode('utf-8')
                if not dados:
                    break
                if 'AVISO' in dados and 'bloqueada' in dados.lower():
                    self.bloqueadas += 1
        except socket.timeout:
            pass
        except Exception:
            pass


def correr_teste(n=5):
    print(f"\n{'='*45}")
    print(f"stress test com {n} clientes - {HOST}:{PORT}")
    print(f"{'='*45}\n")

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

    print(f"\n{'='*45}")
    print("resultado:")
    for c in clientes:
        print(f"  cliente {c.cid}: enviadas={c.enviadas} bloqueadas={c.bloqueadas}")

    print(f"\n  total enviadas:  {total_env}")
    print(f"  total bloqueadas: {total_bloq}")
    if total_env > 0:
        print(f"  taxa bloqueio: {total_bloq / total_env * 100:.1f}%")
    print(f"{'='*45}\n")


if __name__ == '__main__':
    input(f"servidor em {HOST}:{PORT}? enter para comecar: ")
    correr_teste(5)
