import os
import json
import urllib.request

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"

payload = {
    "chat_id": CHAT_ID,
    "question": "🎮 Кто идет играть сегодня?",
    "options": [
        "Буду после 23:00",
        "Буду до 23:00",
        "🤔 Пока не знаю / 50 на 50",
        "❌ Сегодня пас"
    ],
    "is_anonymous": False,           # Открытое голосование (видно ники)
    "allows_multiple_answers": False # Можно выбрать только один вариант
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

with urllib.request.urlopen(req) as response:
    print("Голосование успешно отправлено!")