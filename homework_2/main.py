import re
from collections import Counter


def read_file(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def get_words(text: str) -> list[str]:
    words = re.findall(r"[а-яґєіїa-z]+", text.lower())
    return words


def word_frequency_percentage(text: str) -> dict[str, float]:
    words = get_words(text)
    total_words = len(words)
    if total_words== 0:
        return {}
    counts = Counter(words)
    return{word: round(count/total_words*100, 2) for word, count in counts.items()}


def shortest_word(text: str) -> list[str]:
    words = get_words(text)
    if not words:
        return []
    min_length = min(len(word) for word in words)
    return list({word for word in words if len(word) == min_length})


def longest_word(text: str) -> list[str]:
    words = get_words(text)
    if not words:
        return []
    max_length = max(len(word) for word in words)
    return [word for word in words if len(word) == max_length]


def unique_words(text: str) -> set:
    return set(get_words(text))

def unique_words_count(text: str) -> int:
    return len(unique_words(text))


def word_count(text: str) -> int:
    return len(get_words(text))


def letters_used(text: str) -> str:
    letters = set(re.findall(r"[а-яґєіїa-z]", text.lower()))
    return "".join(sorted(letters))


def most_common_letter(text: str) -> str:
    letters = re.findall(r"[а-яґєіїa-z]", text.lower())
    if not letters:
        return ""
    counts = Counter(letters)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    filepath = "text.txt"
    text = read_file(filepath)

    print("ТЕКСТ:")
    print(text)

    print(f"\n 1) Частотний словник слів (у відсотках): {word_frequency_percentage(text)}")

    print(f"\n 2) Найкоротше(і) слово(а): {shortest_word(text)}")

    print(f"\n 3) Найдовше(і) слово(а): {longest_word(text)}")

    print(f"\n 4) Кількість унікальних слів: {unique_words_count(text)}")

    print(f"\n 5) Кількість слів: {word_count(text)}")

    print(f"\n 6) Використані літери: {letters_used(text)}")

    print(f"\n 7) Найпоширеніша літера: {most_common_letter(text)}")
