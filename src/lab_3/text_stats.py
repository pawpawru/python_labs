import sys
from text import normalize, tokenize, count_freq, top_n

TABLE_MODE = True

def print_top_words(top_n_list):
    """
    Выводит топ-N слов с их частотами в формате, заданном глобальной переменной TABLE_MODE.

    Параметры:
        top_n_list (list[tuple[str, int]]): список кортежей (слово, частота).

    Исключения:
        ValueError: если передан пустой список top_n_list.
    """
    if not top_n_list:
        raise ValueError("Список топ-слов не должен быть пустым.")

    if TABLE_MODE:
        max_word_len = max(len(word) for word, _ in top_n_list)
        header = f"{'слово':<{max_word_len}} | частота"
        separator = "-" * len(header)
        print(header)
        print(separator)
        for word, count in top_n_list:
            print(f"{word:<{max_word_len}} | {count}")
    else:
        for word, count in top_n_list:
            print(f"{word}:{count}")

text = sys.stdin.read()

if not text.strip():
    raise ValueError("Входная строка не должна быть пустой.")

tokens = tokenize(normalize(text))
freq_dict = count_freq(tokens)

total_words = sum(freq_dict.values())
unique_words = len(freq_dict)
top_5 = top_n(freq_dict)

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")

print_top_words(top_5)
