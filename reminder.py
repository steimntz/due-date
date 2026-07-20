import os
import requests
from datetime import date, timedelta

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

DUE_DATE = date(2027, 3, 8)
START_DATE = DUE_DATE - timedelta(weeks=40)

today = date.today()

weeks = (today - START_DATE).days // 7
days = (today - START_DATE).days

if days % 7 == 0:
    message = f"👶 Today begins week {weeks}!"
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message,
        },
    )
