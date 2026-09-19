from backend.app.analyzer import count_fillers, words_per_minute

def test_count_fillers():
    text = "Um, I like basically um think so"
    assert count_fillers(text) == {"um": 2, "like": 1, "basically": 1}

def test_words_per_minute():
    assert words_per_minute("one two three four", 60) == 4.0