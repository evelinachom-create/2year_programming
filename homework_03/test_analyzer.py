import pytest
from analyzer import get_text_from_file, analyze_text

def test_analyze_count_and_frequency():
    text = "Аналіз тексту за допомогою Python. Python — чудова мова програмування для аналізу."
    word_count, freq = analyze_text(text)

    assert word_count == 11
    assert freq["python"] == 2
    assert freq["аналіз"] == 1
    assert freq["аналізу"] == 1
    assert freq["тексту"] == 1


def test_analyze_ignores_case_and_punctuation():
    _, freq = analyze_text("Мова, мова! МОВА?")
    assert freq == {"мова": 3}


def test_analyze_apostrophe_and_hyphen():
    word_count, freq = analyze_text("М'яч і будь-який м'яч")
    assert word_count == 4
    assert freq["м'яч"] == 2


def test_analyze_empty_text_raises_value_error():
    with pytest.raises(ValueError, match="Аналіз неможливий"):
        analyze_text("")
    with pytest.raises(ValueError):
        analyze_text(" ")


def test_analyze_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        analyze_text(123)


def test_read_existing_file(tmp_path):
    f = tmp_path / "text.txt"
    f.write_text("Привіт, світе", encoding="utf-8")
    assert get_text_from_file(str(f)) == "Привіт, світе"


def test_read_missing_file_raises_not_found_error():
    with pytest.raises(FileNotFoundError):
        get_text_from_file("missing_file.txt")


def test_read_empty_file_raises_value_error(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("   ", encoding="utf-8")
    with pytest.raises(ValueError):
        get_text_from_file(str(f))