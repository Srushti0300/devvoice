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


def pace_label(wpm: float) -> str:
    if wpm == 0:
        return "no data"
    if wpm < 110:
        return "too slow"
    if wpm <= 160:
        return "good"
    return "too fast"


def analyze_speech(text: str, seconds: float) -> dict:
    words = len(text.split())
    fillers = count_fillers(text)
    filler_total = sum(fillers.values())
    filler_percent = round(filler_total / words * 100, 1) if words else 0.0
    wpm = words_per_minute(text, seconds)
    return {
        "word_count": words,
        "words_per_minute": wpm,
        "pace": pace_label(wpm),
        "fillers": fillers,
        "filler_percent": filler_percent,
    }