from functools import lru_cache

MODEL_SIZE = "tiny.en"


@lru_cache(maxsize=1)
def get_model():
    from faster_whisper import WhisperModel

    return WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")


def transcribe_audio(path: str) -> tuple[str, float]:
    model = get_model()
    segments, info = model.transcribe(path)
    text = " ".join(segment.text.strip() for segment in segments)
    return text, info.duration