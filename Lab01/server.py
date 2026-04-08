import socket
import threading
import logging

from config import HOST, PORT, BUFFER_SIZE, MAX_CLIENTS
from gdpr_detector import detect_personal_data, has_personal_data
from social_engineering_logger import log_incident

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class ChatServer:

    def __init__(self):
        self.srv = None
        self.clientes = []  # lista de (socket, username)
        self.lock = threading.Lock()  # para nao ter problemas com as threads
        self.ativo = True

    def start(self):
        self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # SO_REUSEADDR evita o "address already in use" ao reiniciar
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.srv.bind((HOST, PORT))
        self.srv.listen(MAX_CLIENTS)
        logger.info(f"servidor a correr em {HOST}:{PORT}")

        try:
            while self.ativo:
                sock, addr = self.srv.accept()
                logger.info(f"novo cliente de {addr}")

                # criar thread para cada cliente novo
                t = threading.Thread(target=self.tratar_cliente, args=(sock, addr))
                t.daemon = True
                t.start()

        except KeyboardInterrupt:
            logger.info("a fechar servidor...")
        finally:
            self.parar()

    def tratar_cliente(self, sock, addr):
        username = None

        try:
            # pedir username ao cliente
            sock.send(b"Username: ")
            username = sock.recv(BUFFER_SIZE).decode('utf-8').strip()

            if not username:
                username = f"user_{addr[1]}"

            # adicionar cliente a lista (com lock para ser thread-safe)
            with self.lock:
                self.clientes.append((sock, username))

            logger.info(f"[CONECTADO] {username} {addr}")

            # avisar os outros que entrou alguem
            self.broadcast(f"[SISTEMA] {username} entrou no chat", excluir=sock)
            sock.send(f"[SISTEMA] Bem-vindo {username}!\n".encode('utf-8'))

            # loop principal - receber mensagens
            while True:
                dados = sock.recv(BUFFER_SIZE).decode('utf-8').strip()

                if not dados:
                    break

                # verificar GDPR antes de fazer broadcast
                if has_personal_data(dados):
                    det = detect_personal_data(dados)
                    logger.warning(f"[BLOQUEADO] {username} - dados: {list(det.keys())}")
                    log_incident(username, dados, det)
                    sock.send(b"[AVISO] Mensagem bloqueada - contem dados pessoais\n")
                    continue

                # mensagem privada comeca com @
                if dados.startswith('@'):
                    self.privada(username, dados)
                else:
                    self.broadcast(f"{username}: {dados}", excluir=sock)

        except Exception as e:
            logger.error(f"erro com {addr}: {e}")

        finally:
            # remover da lista quando desliga
            with self.lock:
                self.clientes = [(s, u) for s, u in self.clientes if s != sock]

            sock.close()
            logger.info(f"[DESCONECTADO] {username} {addr}")

            if username:
                self.broadcast(f"[SISTEMA] {username} saiu do chat")

    def privada(self, remetente, msg):
        # formato esperado: @username mensagem
        partes = msg.split(maxsplit=2)

        if len(partes) < 3:
            return

        destino = partes[0][1:]  # tirar o @
        texto = partes[2]

        sock_destino = None
        with self.lock:
            for s, u in self.clientes:
                if u == destino:
                    sock_destino = s
                    break

        if sock_destino:
            sock_destino.send(f"[PRIVADO de {remetente}] {texto}\n".encode('utf-8'))
            logger.info(f"msg privada: {remetente} -> {destino}")
        else:
            logger.warning(f"utilizador '{destino}' nao esta ligado")

    def broadcast(self, msg, excluir=None):
        msg_bytes = f"{msg}\n".encode('utf-8')
        with self.lock:
            for s, _ in self.clientes:
                if s != excluir:
                    try:
                        s.send(msg_bytes)
                    except:
                        pass  # ignora se o cliente ja desligou entretanto

    def parar(self):
        self.ativo = False
        if self.srv:
            self.srv.close()
        logger.info("servidor fechado")


if __name__ == '__main__':
    s = ChatServer()
    s.start()
