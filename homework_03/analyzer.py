import re
from collections import Counter


def get_text_from_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не знайдено")
    except (UnicodeDecodeError):
        raise ValueError("Не вдалося прочитати файл")

    if text.strip() == "":
        raise ValueError("Файл порожній")
    return text

def get_words(text):
    text = text.lower()
    found = re.findall(r"[a-zA-Zа-яА-ЯіІїЇєЄґҐ'’-]+", text)
    words = []
    for word in found:
        word = word.strip("'’-")
        if word:
            words.append(word)
    return words

def analyze_text(text):
    if not isinstance(text, str):
        raise TypeError("Вхідний текст має бути рядком")
    if text.strip() == "":
        raise ValueError("Аналіз неможливий, текст порожній")

    words = get_words(text)
    return len(words), dict(Counter(words))


if __name__ == "__main__":
    try:
        text = get_text_from_file("text.txt")
    except FileNotFoundError:
        print("Помилка: Файл 'text.txt' не знайдено")
    except ValueError as e:
        print("Помилка:", e)
    else:
        word_count, freq = analyze_text(text)
        print("Кількість слів:", word_count)
        print("Частотність:", freq)