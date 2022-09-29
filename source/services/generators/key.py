from datetime import datetime
from hashlib import md5
from os import system


def generate_key(telegram_id: int) -> str:
    time = datetime.now().strftime('%d-%h-%Y %r') 
    user = str(telegram_id)
    raw_key = time + user
    return md5(raw_key.encode()).hexdigest()

