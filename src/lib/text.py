def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализовать текст

    Args:
        text: строка
        casefold: приводить ли буквы к нижнему регистру
        yo2e: заменять ли "ё" на е
    
    Returns:
        text: нормализированный текст
    """
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё", "е")
    text = text.strip()
    text = " ".join(text.split())
    return text

import re

def tokenize(text: str) -> list[str]:
    """
    Разбить на слова (токены)

    Args:
        text: строка для токенизации
    
    Returns:
        list[str]: список слов (токенов), где словом считается последовательность символов (буквы, цифры, подчёркивание) с дефисами внутри слова
    """
    pattern = r'[\w]+(?:-[\w]+)*'
    return re.findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Посчитать количество повторений токенов

    Args:
        tokens: список токенов

    Returns:
        freq: словарь вида: [слово] -> [количество повторений]
    """
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова

    Args:
        freq: слловарь вида: [слово] -> [количество повторений]
        n: количество элементов топа
    
    Returns:
        data: список кортежей вида: (токен, количество повторений)
    """
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
if __name__ == "__main__":
    print(r"ПрИвЕт\nМИр\t ->", normalize("ПрИвЕт\nМИр\t"))
    print("ёжик, Ёлка ->", normalize("ёжик, Ёлка"))
    print(r"Hello\r\nWorld ->", normalize("Hello\r\nWorld"))
    print("  двойные   пробелы   ->", normalize("  двойные   пробелы  "))

    print("привет мир ->", tokenize("привет мир"))
    print("hello,world!!! ->", tokenize("hello,world!!!"))
    print("по-настоящему круто ->", tokenize("по-настоящему круто"))
    print("2025 год ->", tokenize("2025 год"))
    print("emoji 😀 не слово ->", tokenize("emoji 😀 не слово"))

    print('["a","b","a","c","b","a"] ->', count_freq(["a","b","a","c","b","a"]))
    print('["bb","aa","bb","aa","cc"] ->', count_freq(["bb","aa","bb","aa","cc"]))

    print(count_freq(["a","b","a","c","b","a"]), '->', top_n(count_freq(["a","b","a","c","b","a"]), n = 2))
    print(count_freq(["bb","aa","bb","aa","cc"]), '->', top_n(count_freq(["bb","aa","bb","aa","cc"]), n = 2))