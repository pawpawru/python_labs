import sys
from text import normalize, tokenize, count_freq, top_n

TABLE_MODE = False

def print_top_words(top_words, use_table: bool):
    if not top_words:
        raise TypeError("Нет слов для отображения.")
        return

    if use_table:
        max_word_len = max(len(word) for word, _ in top_words)
        header = f"{'слово':<{max_word_len}} | частота"
        separator = "-" * len(header)
        print(header)
        print(separator)
        for word, count in top_words:
            print(f"{word:<{max_word_len}} | {count}")
    else:
        for word, count in top_words:
            print(f"{word}:{count}")

def analyze_text(text: str, use_table: bool):
    if not text.strip():
        print("Входной текст пуст.")
        return

    tokens = tokenize(normalize(text))
    
    if not tokens:
        raise TypeError("В тексте не найдено слов для анализа.")
        return

    freq_dict = count_freq(tokens)
    total_words = sum(freq_dict.values())
    unique_words = len(freq_dict)
    top_5 = top_n(freq_dict)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")

    print_top_words(top_5, use_table)

if __name__ == "__main__":
    text = sys.stdin.read()
    analyze_text(text, TABLE_MODE)

