import json
import logging
from datetime import datetime

from config import INCIDENTS_FILE

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def log_incident(username, mensagem, dados_detetados):
    try:
        tipos = list(dados_detetados.keys())

        novo = {
            'timestamp': datetime.now().isoformat(),
            'username': username,
            'original_message': mensagem[:500],
            'detected_data_types': tipos
        }

        # ler o que ja existe no ficheiro
        try:
            with open(INCIDENTS_FILE, 'r') as f:
                lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            lista = []

        lista.append(novo)

        with open(INCIDENTS_FILE, 'w') as f:
            json.dump(lista, f, indent=2, ensure_ascii=False)

        logger.info(f"incidente guardado - {username}: {tipos}")
        return True

    except Exception as e:
        logger.error(f"erro ao guardar: {e}")
        return False


def get_incidents_by_user(username):
    try:
        with open(INCIDENTS_FILE, 'r') as f:
            lista = json.load(f)
        return [x for x in lista if x['username'] == username]
    except FileNotFoundError:
        return []
    except Exception as e:
        logger.error(f"erro: {e}")
        return []


def get_all_incidents():
    try:
        with open(INCIDENTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        logger.error(f"erro: {e}")
        return []
