from backend.app.analyzer import (
    count_fillers,
    words_per_minute,
    pace_label,
    analyze_speech,
)


def test_count_fillers():
    text = "Um, I like basically um think so"
    assert count_fillers(text) == {"um": 2, "like": 1, "basically": 1}


def test_words_per_minute():
    assert words_per_minute("one two three four", 60) == 4.0


def test_pace_label():
    assert pace_label(90) == "too slow"
    assert pace_label(140) == "good"
    assert pace_label(200) == "too fast"


def test_analyze_speech():
    result = analyze_speech("um I like coding", 60)
    assert result["word_count"] == 4
    assert result["fillers"] == {"um": 1, "like": 1}
    assert result["filler_percent"] == 50.0