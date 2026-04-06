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
        self.clientes = []  # lista de tuplos (socket, username)
        self.lock = threading.Lock()
        self.ativo = True

    def start(self):
        self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.srv.bind((HOST, PORT))
            self.srv.listen(MAX_CLIENTS)
            logger.info(f"servidor a correr em {HOST}:{PORT}")

            while self.ativo:
                try:
                    sock, addr = self.srv.accept()
                    logger.info(f"nova ligacao de {addr}")

                    t = threading.Thread(target=self.tratar_cliente, args=(sock, addr))
                    t.daemon = True
                    t.start()

                except Exception as e:
                    if self.ativo:
                        logger.error(f"erro ao aceitar ligacao: {e}")

        except KeyboardInterrupt:
            logger.info("ctrl+c detetado, a fechar...")
        finally:
            self.parar()

    def tratar_cliente(self, sock, addr):
        username = None

        try:
            sock.send(b"Username: ")
            username = sock.recv(BUFFER_SIZE).decode('utf-8').strip()

            if not username:
                username = f"user_{addr[1]}"

            with self.lock:
                self.clientes.append((sock, username))

            logger.info(f"[CONECTADO] {username} - {addr}")
            self.broadcast(f"[SISTEMA] {username} entrou no chat", excluir=sock)
            sock.send(f"[SISTEMA] Bem-vindo {username}!\n".encode('utf-8'))

            while True:
                dados = sock.recv(BUFFER_SIZE).decode('utf-8').strip()

                if not dados:
                    break

                # antes de enviar verificar se tem dados pessoais
                if has_personal_data(dados):
                    det = detect_personal_data(dados)
                    logger.warning(f"[BLOQUEADO] {username} tentou enviar dados pessoais: {list(det.keys())}")
                    log_incident(username, dados, det)
                    sock.send(b"[AVISO] Mensagem bloqueada - contem dados pessoais\n")
                    continue

                if dados.startswith('@'):
                    self.privada(username, dados)
                else:
                    self.broadcast(f"{username}: {dados}", excluir=sock)

        except Exception as e:
            logger.error(f"erro com cliente {addr}: {e}")

        finally:
            with self.lock:
                self.clientes = [(s, u) for s, u in self.clientes if s != sock]
            sock.close()
            logger.info(f"[DESCONECTADO] {username} - {addr}")
            if username:
                self.broadcast(f"[SISTEMA] {username} saiu do chat")

    def privada(self, remetente, msg):
        # formato: @destino mensagem
        partes = msg.split(maxsplit=2)
        if len(partes) < 3:
            return

        dest = partes[0][1:]
        texto = partes[2]

        alvo = None
        with self.lock:
            for s, u in self.clientes:
                if u == dest:
                    alvo = s
                    break

        if alvo:
            try:
                alvo.send(f"[PRIVADO de {remetente}] {texto}\n".encode('utf-8'))
                logger.info(f"privada: {remetente} -> {dest}")
            except:
                pass
        else:
            logger.warning(f"utilizador {dest} nao encontrado para msg privada")

    def broadcast(self, msg, excluir=None):
        b = f"{msg}\n".encode('utf-8')
        with self.lock:
            for s, _ in self.clientes:
                if s != excluir:
                    try:
                        s.send(b)
                    except:
                        pass

    def parar(self):
        self.ativo = False
        if self.srv:
            self.srv.close()
        logger.info("servidor fechado")


if __name__ == '__main__':
    s = ChatServer()
    s.start()
