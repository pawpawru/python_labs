def test(func, data, description=None):
    """
    Выполняет функцию и выводит результат в формате: '<описание> -> <результат>'.

    Args:
        func: функция, которую нужно применить к данным.
        data: входные данные для функции.
        description: текстовое описание входных данных для вывода. Если не указано,
                     формируется автоматически на основе repr(data).

    Returns:
        None: функция только печатает результат, ничего не возвращает.
    """
    result = func(data)
      
    if description is None:
        description = repr(data)
    
    print(f"{description} -> {result}")