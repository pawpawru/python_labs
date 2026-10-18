from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает файл и возвращает его содержимое одной строкой.

    Важно: весь файл загружается в память - не следует использовать для больших файлов
    (сотни МБ и больше). Для них лучше обрабатывать данные по частям или построчно.

    Пример выбора другой кодировки:
        text = read_text("data/lab04/input.txt", encoding="cp1251")

    Args:
        path: путь к файлу (строка или Path).
        encoding: кодировка файла (по умолчанию utf-8, можно передать, например, "cp1251").

    Returns:
        Содержимое файла как строка. Для пустого файла - пустая строка.

    Raises:
        FileNotFoundError: если файл не найден.
        UnicodeDecodeError: если кодировка не подходит.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские папки для указанного пути, если их нет.

    Args:
        path: путь к файлу или папке.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """
    Записывает данные в CSV-файл с разделителем ','. Если файл уже есть - перезапишет его.

    Особенности:
        - Если rows пустой и header не задан - создаётся пустой файл.
        - Если rows пустой, но header задан - в файле будет только заголовок.

    Args:
        rows: строки данных (каждая - последовательность значений одинаковой длины).
        path: путь к CSV-файлу.
        header: необязательный заголовок таблицы.

    Raises:
        ValueError: если строки в rows имеют разную длину (или не совпадают с длиной header).
        OSError: при проблемах с доступом к файлу.
    """
    p = Path(path)
    rows_list = list(rows)

    # Проверка одинаковой длины всех строк в rows
    if rows_list:
        expected_len = len(rows_list[0])
        for i, r in enumerate(rows_list):
            if len(r) != expected_len:
                raise ValueError(
                    f"Строка {i} имеет длину {len(r)}, ожидалось {expected_len}"
                )
        if header is not None and len(header) != expected_len:
            raise ValueError(
                f"Длина заголовка ({len(header)}) не совпадает с длиной строк ({expected_len})"
            )

    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows_list:
            w.writerow(r)


if __name__ == "__main__":
    txt = read_text("data/lab_4/input.txt")  # должен вернуть строку
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab_4/check.csv")  # создаст CSV
    print("CSV создан")