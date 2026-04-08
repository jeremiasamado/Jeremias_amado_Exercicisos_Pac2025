import json
import logging
from datetime import datetime

from config import INCIDENTS_FILE

# so para ver o que esta a acontecer no terminal
logger = logging.getLogger(__name__)


def log_incident(username, mensagem, dados_detetados):
    # guarda o incidente no ficheiro json
    # se o ficheiro nao existir cria um novo com lista vazia

    try:
        tipos_encontrados = list(dados_detetados.keys())

        incidente = {
            'timestamp': datetime.now().isoformat(),
            'username': username,
            'original_message': mensagem[:500],
            'detected_data_types': tipos_encontrados
        }

        # tentar ler incidentes ja existentes
        try:
            with open(INCIDENTS_FILE, 'r') as f:
                lista = json.load(f)
        except FileNotFoundError:
            lista = []
        except json.JSONDecodeError:
            # ficheiro existe mas esta corrompido ou vazio
            lista = []

        lista.append(incidente)

        with open(INCIDENTS_FILE, 'w') as f:
            json.dump(lista, f, indent=2, ensure_ascii=False)

        logger.info(f"incidente guardado para {username} - {tipos_encontrados}")
        return True

    except Exception as e:
        logger.error(f"nao conseguiu guardar incidente: {e}")
        return False


def get_incidents_by_user(username):
    # devolve lista de incidentes de um utilizador especifico
    try:
        with open(INCIDENTS_FILE, 'r') as f:
            lista = json.load(f)

        resultado = []
        for item in lista:
            if item['username'] == username:
                resultado.append(item)

        return resultado

    except FileNotFoundError:
        return []
    except Exception as e:
        logger.error(f"erro ao ler incidents: {e}")
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
