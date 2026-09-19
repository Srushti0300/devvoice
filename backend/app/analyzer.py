import re

FILLERS = ["um", "uh", "like", "you know", "basically", "actually"]

def count_fillers(text: str) -> dict:
    text = text.lower()
    result = {}
    for f in FILLERS:
        n = len(re.findall(rf"\b{re.escape(f)}\b", text))
        if n:
            result[f] = n
    return result

def words_per_minute(text: str, seconds: float) -> float:
    if seconds <= 0:
        return 0.0
    return round(len(text.split()) / (seconds / 60), 1)