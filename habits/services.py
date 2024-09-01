import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN_BOT


def send_telegram_message(telegram_id, message):
    print("test")
    params = {
        "text": message,
        "chat_id": telegram_id,
    }
    print(TELEGRAM_TOKEN_BOT)
    requests.post(f'{TELEGRAM_URL}{TELEGRAM_TOKEN_BOT}/sendMessage?', params=params)
