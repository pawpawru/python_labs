import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в формат CSV.

    Параметры:
        json_path: Относительный или абсолютный путь к исходному файлу JSON.
        csv_path: Относительный или абсолютный путь к итоговому файлу CSV.

    Исключения:
        FileNotFoundError: Если исходный JSON-файл отсутствует.
        ValueError: Если указан неверный формат файла, JSON пуст, поврежден,
                    не является списком словарей или отсутствуют заголовки.
    """
    input_file = Path(json_path)
    output_file = Path(csv_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    if input_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный тип файла: ожидался .json, получен {input_file.suffix}")

    try:
        with input_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    all_keys = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError(f"Ожидался словарь, получен {type(item).__name__}")
        for key in item.keys():
            all_keys.append(key)

    fieldnames = list(dict.fromkeys(all_keys))
    if not fieldnames:
        raise ValueError("CSV без заголовка или пустой")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV-файл в JSON (список словарей).

    Параметры:
        csv_path: Относительный или абсолютный путь к исходному файлу CSV.
        json_path: Относительный или абсолютный путь к итоговому файлу JSON.

    Исключения:
        FileNotFoundError: Если исходный CSV-файл отсутствует.
        ValueError: Если расширение не .csv, заголовок отсутствует, пуст
                    или в файле нет строк с данными.
    """
    input_file = Path(csv_path)
    output_file = Path(json_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    if input_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: ожидался .csv, получен {input_file.suffix}")

    rows = []
    with input_file.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None or len(reader.fieldnames) == 0:
            raise ValueError("CSV без заголовка или пустой")

        if all(col is None or col.strip() == "" for col in reader.fieldnames):
            raise ValueError("CSV без заголовка или пустой")

        for row in reader:
            rows.append(row)

    if len(rows) == 0:
        raise ValueError("Пустой JSON или CSV")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")