from pathlib import Path
import csv
from typing import Iterable, Sequence


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


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские папки для указанного пути, если их нет.

    Args:
        path: путь к файлу или папке.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    txt = read_text("data\\lab_4\\input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data\\lab_4\\check.csv")
    print("CSV создан")