import json
import os
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

        incidente = {
            'timestamp': datetime.now().isoformat(),
            'username': username,
            'original_message': mensagem[:500],
            'detected_data_types': tipos
        }

        # ler ficheiro existente ou comecar do zero
        try:
            with open(INCIDENTS_FILE, 'r') as f:
                lista = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            lista = []

        lista.append(incidente)

        with open(INCIDENTS_FILE, 'w') as f:
            json.dump(lista, f, indent=2, ensure_ascii=False)

        logger.info(f"Incidente guardado para {username}: {tipos}")
        return True

    except Exception as e:
        logger.error(f"Erro ao guardar incidente: {e}")
        return False


def get_incidents_by_user(username):
    try:
        with open(INCIDENTS_FILE, 'r') as f:
            lista = json.load(f)

        return [i for i in lista if i['username'] == username]

    except FileNotFoundError:
        return []
    except Exception as e:
        logger.error(f"Erro: {e}")
        return []


def get_all_incidents():
    try:
        with open(INCIDENTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        logger.error(f"Erro: {e}")
        return []
