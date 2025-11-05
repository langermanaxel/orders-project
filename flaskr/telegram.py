import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
DEFAULT_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(message: str):
    """Envía mensaje al chat principal (por ejemplo al admin o grupo)."""
    if not TOKEN or not DEFAULT_CHAT_ID:
        print("[Telegram OFF] Mensaje:", message)
        return
    _send_message(DEFAULT_CHAT_ID, message)


def send_telegram_message_to(message: str, chat_id: str):
    """Envía mensaje directo a un chat específico (cliente)."""
    if not TOKEN or not chat_id:
        print("[Telegram OFF] (sin chat_id) Mensaje:", message)
        return
    _send_message(chat_id, message)


def _send_message(chat_id, message):
    """Función interna para enviar el mensaje real."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print("Error al enviar mensaje Telegram:", e)
