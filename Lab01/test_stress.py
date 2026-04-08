import socket
import threading
import time

from config import HOST, PORT, BUFFER_SIZE

# script para testar o servidor com varios clientes ao mesmo tempo
# cada cliente envia mensagens normais e com dados pessoais


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

            print(f"[cliente {self.cid}] ligado")

            self.sock.recv(BUFFER_SIZE)  # username prompt
            self.sock.send(self.username.encode('utf-8'))
            self.sock.recv(BUFFER_SIZE)  # boas vindas

            # teste 1 - mensagem normal, nao deve ser bloqueada
            self.mandar("ola a todos")

            # teste 2 - com email, deve ser bloqueada
            self.mandar(f"o meu email: teste{self.cid}@mail.com")

            # teste 3 - com telefone, deve ser bloqueada
            self.mandar("o meu numero e 912345678")

            time.sleep(2)
            self.ler_respostas()
            self.sock.close()

            print(f"[cliente {self.cid}] fim | enviadas: {self.enviadas} bloqueadas: {self.bloqueadas}")

        except Exception as e:
            print(f"[cliente {self.cid}] erro: {e}")

    def mandar(self, msg):
        try:
            self.sock.send(msg.encode('utf-8'))
            self.enviadas += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"[cliente {self.cid}] erro ao enviar: {e}")

    def ler_respostas(self):
        # ler tudo o que o servidor mandou de volta
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
    print(f"stress test - {n} clientes em simultaneo")
    print(f"{'='*45}\n")

    clientes = []
    for i in range(n):
        c = ClienteTeste(i)
        clientes.append(c)
        c.start()
        time.sleep(0.5)

    # esperar que todos acabem
    for c in clientes:
        c.join()

    # contar totais
    total_bloq = 0
    total_env = 0
    for c in clientes:
        total_bloq = total_bloq + c.bloqueadas
        total_env = total_env + c.enviadas

    print(f"\n{'='*45}")
    print("relatorio final:")
    print(f"{'='*45}")
    for c in clientes:
        print(f"  cliente {c.cid}: enviadas={c.enviadas}  bloqueadas={c.bloqueadas}")

    print(f"\n  total enviadas:   {total_env}")
    print(f"  total bloqueadas: {total_bloq}")
    if total_env > 0:
        perc = total_bloq / total_env * 100
        print(f"  taxa de bloqueio: {perc:.1f}%")
    print(f"{'='*45}\n")


if __name__ == '__main__':
    input(f"confirmar que o servidor esta em {HOST}:{PORT} e carregar enter... ")
    correr_teste(5)
