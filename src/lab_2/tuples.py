def format_record(rec: tuple[str, str, float]) -> str:
    """
    Параметры:
        rec: кортеж вида: (fio: str, group: str, gpa: float).
            
    Возвращает:
        Строка вида: Иванов И.И., гр. BIVT-25, GPA 4.60.
            
    Вызывает:
        ValueError: если пустое ФИО или пустая группа.
        TypeError: если неверный тип GPA.
    """
    if not rec[0]:
        raise ValueError("пустое ФИО")
    if not rec[1]:
        raise ValueError("пустая группа")
    if not isinstance(rec[2], float):
        raise TypeError("неверный тип GPA")
    initials = rec[0]
    initials = str.title(initials)
    initials = [i for i in initials.split()]
    last_name = initials[0]
    if len(initials) == 2:
        name = initials[1][0] + '.'
        patronymic = ''
    elif len(initials) == 3:
        name = initials[1][0] + '.'
        patronymic = initials[2][0] + '.'
    group = rec[1]
    gpa = rec[2]
    return f'{last_name} {name}{patronymic}, гр. {group}, GPA {gpa:.2f}'
if __name__ == "__main__":
    print('("Иванов Иван Иванович", "BIVT-25", 4.6) ->', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print('("Петров Пётр", "IKBO-12", 5.0) ->', format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print('("Петров Пётр Петрович", "IKBO-12", 5.0) ->', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999) ->', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))