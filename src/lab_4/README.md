Лаботаторная работа № 4

Задание A

```python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает файл и возвращает его содержимое одной строкой.

    Важно: весь файл загружается в память - не следует использовать для больших файлов
    (сотни МБ и больше). Для них лучше обрабатывать данные по частям или построчно.

    Args:
        path: путь к файлу (строка или Path).
        encoding: кодировка файла (по умолчанию utf-8).

    Returns:
        Содержимое файла как строка. Для пустого файла - пустая строка.

    Raises:
        FileNotFoundError: если файл не найден.
        UnicodeDecodeError: если кодировка не подходит.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)
```

```python
def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """
    Записывает данные в CSV-файл. Если файл уже есть - перезапишет его.

    Особенности:
        - Если rows пустой и header не задан - создаётся пустой файл.
        - Если rows пустой, но header задан - в файле будет только заголовок.

    Args:
        rows: строки данных (каждая - последовательность значений).
        path: путь к CSV-файлу.
        header: необязательный заголовок таблицы.

    Raises:
        OSError: при проблемах с доступом к файлу.
        TypeError: если строки не являются последовательностями.
    """
    p = Path(path)
    rows_list = list(rows)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows_list:
            w.writerow(r)
```

```python
def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские папки для указанного пути, если их нет.

    Args:
        path: путь к файлу или папке.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
```

Тесты:
```python
if __name__ == "__main__":
    txt = read_text("data\\lab_4\\input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data\\lab_4\\check.csv")
    print("CSV создан")
```
![Тесты io_txt_csv.py](../../images/lab_4/img_03.png)

Задание B
```python
from lib.text import normalize, tokenize, count_freq, top_n
from lab_4.io_txt_csv import read_text, write_csv

INPUT_PATH = "..\\data\\lab_4\\input.txt"
OUTPUT_PATH = "..\\data\\lab_4\\report.csv"
ENCODING = "utf-8"

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))


def main():
    try:
        raw_text = read_text(INPUT_PATH, encoding=ENCODING)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {INPUT_PATH}")
        return

    normalized_text = normalize(raw_text)
    tokens = tokenize(normalized_text)
    total_words = len(tokens)

    freq = count_freq(tokens)
    unique_words = len(freq)

    all_rows = sorted_word_counts(freq)
    top5 = top_n(freq, n=5)

    write_csv(all_rows, OUTPUT_PATH, header=("word", "count"))

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5: ")
    for word, count in top5:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
```
вход:

'![input.txt](../../images/lab_4/img_04.png)'

консоль:

![консоль](../../images/lab_4/img_01.png)

report.csv:

![report.txt](../../images/lab_4/img_02.png)