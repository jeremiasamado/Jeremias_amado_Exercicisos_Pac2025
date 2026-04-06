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
        self.server_socket = None
        # lista de (socket, username)
        self.clientes = []
        self.lock = threading.Lock()
        self.a_correr = True

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server_socket.bind((HOST, PORT))
            self.server_socket.listen(MAX_CLIENTS)
            logger.info(f"Servidor iniciado em {HOST}:{PORT}")

            while self.a_correr:
                try:
                    cliente_socket, endereco = self.server_socket.accept()
                    logger.info(f"Conexao de {endereco}")

                    t = threading.Thread(
                        target=self.tratar_cliente,
                        args=(cliente_socket, endereco)
                    )
                    t.daemon = True
                    t.start()

                except Exception as e:
                    if self.a_correr:
                        logger.error(f"Erro ao aceitar: {e}")

        except KeyboardInterrupt:
            logger.info("A encerrar servidor...")
        finally:
            self.parar()

    def tratar_cliente(self, cliente_socket, endereco):
        username = None

        try:
            cliente_socket.send(b"Username: ")
            username = cliente_socket.recv(BUFFER_SIZE).decode('utf-8').strip()

            if not username:
                username = f"user_{endereco[1]}"

            with self.lock:
                self.clientes.append((cliente_socket, username))

            logger.info(f"[CONECTADO] {username} {endereco}")
            self.broadcast(f"[SISTEMA] {username} entrou no chat", excluir=cliente_socket)
            cliente_socket.send(f"[SISTEMA] Bem-vindo {username}!\n".encode('utf-8'))

            while True:
                dados = cliente_socket.recv(BUFFER_SIZE).decode('utf-8').strip()

                if not dados:
                    break

                # verificar gdpr antes de enviar
                if has_personal_data(dados):
                    detetado = detect_personal_data(dados)
                    logger.warning(f"[BLOQUEADO] mensagem de {username} com dados pessoais")
                    log_incident(username, dados, detetado)
                    cliente_socket.send(b"[AVISO] Mensagem bloqueada - contem dados pessoais\n")
                    continue

                if dados.startswith('@'):
                    self.mensagem_privada(username, dados)
                else:
                    self.broadcast(f"{username}: {dados}", excluir=cliente_socket)

        except Exception as e:
            logger.error(f"Erro com {endereco}: {e}")

        finally:
            with self.lock:
                self.clientes = [(s, u) for s, u in self.clientes if s != cliente_socket]

            cliente_socket.close()
            logger.info(f"[DESCONECTADO] {username} {endereco}")

            if username:
                self.broadcast(f"[SISTEMA] {username} saiu do chat")

    def mensagem_privada(self, remetente, msg):
        partes = msg.split(maxsplit=2)

        if len(partes) < 3:
            return

        destino_nome = partes[0][1:]  # tirar o @
        texto = partes[2]

        destino_socket = None
        with self.lock:
            for s, u in self.clientes:
                if u == destino_nome:
                    destino_socket = s
                    break

        if destino_socket:
            try:
                destino_socket.send(f"[PRIVADO de {remetente}] {texto}\n".encode('utf-8'))
                logger.info(f"[PRIVADO] {remetente} -> {destino_nome}")
            except:
                pass
        else:
            logger.warning(f"Utilizador {destino_nome} nao encontrado")

    def broadcast(self, msg, excluir=None):
        msg_bytes = f"{msg}\n".encode('utf-8')
        with self.lock:
            for s, _ in self.clientes:
                if s != excluir:
                    try:
                        s.send(msg_bytes)
                    except:
                        pass

    def parar(self):
        self.a_correr = False
        if self.server_socket:
            self.server_socket.close()
        logger.info("Servidor encerrado")


if __name__ == '__main__':
    servidor = ChatServer()
    servidor.start()
