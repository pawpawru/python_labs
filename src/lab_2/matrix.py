def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Параметры:
        mat: матрица.
    
    Возвращает:
        Транспонированная матрица.
    
    Вызывает:
        ValueError: если строки разной длины.
    '''
    if not mat:
        return []
    if not all(len(i) == len(mat[0]) for i in mat):
        raise ValueError("Есть строки разной длины")
# функция ещё не доделана