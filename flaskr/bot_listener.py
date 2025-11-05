import os
import time
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
DB_PATH = os.path.join("instance", "flaskr.sqlite")

def save_chat_id(name_or_phone, chat_id):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("""
        UPDATE order
        SET customer_chat_id = ?
        WHERE customer_name LIKE ? OR customer_tel LIKE ?
    """, (chat_id, f"%{name_or_phone}%", f"%{name_or_phone}%"))
    con.commit()
    con.close()

def main():
    offset = 0
    print("🟢 Escuchando mensajes de Telegram...")
    while True:
        resp = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={offset}").json()
        for update in resp.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message")
            if not msg:
                continue
            chat_id = msg["chat"]["id"]
            text = msg.get("text", "").strip()
            print(f"📩 Mensaje de {chat_id}: {text}")

            if text:
                save_chat_id(text, chat_id)
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={
                    "chat_id": chat_id,
                    "text": "✅ ¡Listo! Te vinculamos con tus pedidos. Te avisaremos cuando cambie el estado."
                })
        time.sleep(2)

if __name__ == "__main__":
    main()
