def format_record(rec: tuple[str, str, float]) -> str:
    """
    Параметры:
        rec: кортеж вида: (fio: str, group: str, gpa: float).

    Возвращает:
        Строка вида: Иванов И.И., гр. BIVT-25, GPA 4.60.

    Вызывает:
        TypeError:
            - если rec не является кортежем;
            - если ФИО или группа не являются строками;
            - если GPA не является числом.
        ValueError:
            - если кортеж содержит не 3 элемента;
            - если после удаления пробелов ФИО оказывается пустым;
            - если после удаления пробелов группа оказывается пустой;
            - если количество частей в ФИО не равно 2 или 3;
            - если значение GPA выходит за диапазон [0.0, 5.0].
    """
    if not isinstance(rec, tuple):
        raise TypeError("rec должен быть кортежем")
    if len(rec) != 3:
        raise ValueError("кортеж должен содержать 3 элемента")

    fio, group, gpa = rec

    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("группа должна быть строкой")
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом (int или float)")

    normalized_fio = " ".join(fio.split())
    normalized_group = " ".join(group.split())

    if not normalized_fio:
        raise ValueError("пустое ФИО")
    if not normalized_group:
        raise ValueError("пустая группа")

    gpa_value = float(gpa)
    if not (0.0 <= gpa_value <= 5.0):
        raise ValueError("неверное значение GPA (должно быть от 0.0 до 5.0)")

    parts = normalized_fio.split()
    if len(parts) not in (2, 3):
        raise ValueError("ФИО должно состоять из 2 или 3 слов")

    last_name = parts[0].capitalize()
    name_initial = parts[1][0].upper() + "."

    patronymic_initial = ""
    if len(parts) == 3:
        patronymic_initial = parts[2][0].upper() + "."

    return f"{last_name} {name_initial}{patronymic_initial}, гр. {normalized_group}, GPA {gpa_value:.2f}"

if __name__ == "__main__":
    print(f'("Иванов Иван Иванович", "BIVT-25", 4.6) -> "{format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}"')
    print(f'("Петров Пётр", "IKBO-12", 5.0) -> "{format_record(("Петров Пётр", "IKBO-12", 5.0))}"')
    print(f'("Петров Пётр Петрович", "IKBO-12", 5.0) -> "{format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}"')
    print(f'("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> "{format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}"')
