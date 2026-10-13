Лаботаторная работа № 3

Задание A
```python
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
    if type(text) != str:
        raise TypeError('не тот тип данных')
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё", "е")
    text = text.strip()
    text = " ".join(text.split())
    return text
```
![Вывод normalize](../../images/lab_3/img_01.png)

Рис. 1. Результат выполнения функции normalize

```python
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
```
![Вывод tokenize](../../images/lab_3/img_02.png)

Рис. 2. Результат выполнения функции tokenize

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Посчитать количество повторений токенов

    Args:
        tokens: список токенов

    Returns:
        freq: словарь вида: [слово] -> [количество повторений]
    """
    if type(tokens) != list:
        raise TypeError('не правильный тип входных данных')
    if len(tokens) == 0:
        raise ValueError('пустой список')
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq
```
![Вывод count_freq](../../images/lab_3/img_03.png)

Рис. 3. Результат выполнения функции count_freq

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова

    Args:
        freq: слловарь вида: [слово] -> [количество повторений]
        n: количество элементов топа
    
    Returns:
        data: список кортежей вида: (токен, количество повторений)
    """
    if type(freq) != list:
            raise TypeError('не правильный тип входных данных')
    if len(freq) == 0:
        raise ValueError('пустой список')
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```
![Вывод top_n](../../images/lab_3/img_04.png)

Рис. 4. Результат выполнения функции top_n

Задание B

Скрипт читает весь ввод до EOF
```python
from lib.text import normalize, tokenize, count_freq, top_n

TABLE_MODE = False

def main():
    text = input()

    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top_words = top_n(freq)

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(freq.items())}')
    print('Топ-5:')

    if TABLE_MODE:
        if top_words:
            width = max(len(word) for word, count in top_words)

            print(f'{'слово':<{width}} | частота')
            print('-' * (width + 10))

            for word, count in top_words:
                print(f'{word:<{width}} | {count}')

    else:
        for word, count in top_words:
            print(f'{word}:{count}')

if __name__ == "__main__":
    main()
```
![Вывод text_stats_1](../../images/lab_3/img_05.png)

Рис. 5. Результат выполнения text_stats если TABLE_MODE = True

![Вывод text_stats_2](../../images/lab_3/img_06.png)

Рис. 6. Результат выполнения text_stats если TABLE_MODE = False