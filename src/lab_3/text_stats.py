import sys
from text import normalize, tokenize, count_freq, top_n

TABLE_MODE = True

text = sys.stdin.read()
tokens = tokenize(normalize(text))
freq_dict = count_freq(tokens)

total_words = sum(freq_dict.values())
unique_words = len(freq_dict)
top_5 = top_n(freq_dict)

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")

if TABLE_MODE:
    max_word_len = max(len(word) for word, _ in top_5)
    header = f"{'слово':<{max_word_len}} | частота"
    separator = "-" * len(header)
    print(header)
    print(separator)
    for word, count in top_5:
        print(f"{word:<{max_word_len}} | {count}")
else:
    for word, count in top_5:
        print(f"{word}:{count}")
