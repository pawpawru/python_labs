import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    input_file = Path(csv_path)
    output_file = Path(xlsx_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    if input_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: ожидался .csv, получен {input_file.suffix}")

    with input_file.open("r", encoding="utf-8") as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("CSV без заголовка или пустой")

    header = reader[0]
    if not header or all(str(cell).strip() == "" for cell in header):
        raise ValueError("CSV без заголовка или пустой")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_len = 0
        col_letter = col[0].column_letter
        for cell in col:
            val_str = str(cell.value) if cell.value is not None else ""
            if len(val_str) > max_len:
                max_len = len(val_str)
        ws.column_dimensions[col_letter].width = max(max_len + 2, 8)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    wb.save(str(output_file))


if __name__ == "__main__":
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
    
