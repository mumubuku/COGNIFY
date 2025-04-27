from datetime import datetime

def now_timestamp() -> str:
    return datetime.utcnow().isoformat() + 'Z'