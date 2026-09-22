def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Параметры:
        mat: матрица.
    
    Возвращает:
        Транспонированная матрица.
    
    Вызывает:
        ValueError: если строки разной длины (не прямоугольная матрица).
    """
    if not mat:
        return []
    elif not all(len(i) == len(mat[0]) for i in mat):
        raise ValueError("Есть строки разной длины")
    else:
        rows_len = len(mat)
        columns_len = len(mat[0])
        '''
        чтобы проверить что это работает именно так я рассмотрел 2 матрицы:
        1 2 3
        4 5 6

        1 2 3 4
        5 6 7 8

        можно заметить, что длина строки == количеству столбцов при условии, что все строки одной длины.
        '''
        transposed_mat = [[0] * rows_len for i in range(columns_len)]
        for rows in range(rows_len):
            for columns in range(columns_len):
                transposed_mat[columns][rows] = mat[rows][columns]
        return transposed_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Параметры:
        mat: матрица.
        
    Возвращает:
        Сумма каждой строки.
        
    Вызывает:
        ValueError: если строки разной длины (не прямоугольная матрица).
    """
    if not mat:
        return "Пустая матрица"
    elif not all(len(i) == len(mat[0]) for i in mat):
        raise ValueError("Есть строки разной длины")
    else:
        return [sum(i) for i in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Параметры:
        mat: матрица.
        
    Возвращает:
        Сумма каждого столбца.
        
    Вызывает:
        ValueError: если строки разной длины (не прямоугольная матрица).    
    """
    if not mat:
            return "Пустая матрица"
    elif not all(len(i) == len(mat[0]) for i in mat):
        raise ValueError("Есть строки разной длины")
    else:
        return row_sums(transpose(mat))
                
if __name__ == "__main__":
    # TEST transpose
    print('[[1, 2, 3]] ->', transpose([[1, 2, 3]]))
    print('[[1], [2], [3]] ->', transpose([[1], [2], [3]]))
    print('[[1, 2], [3, 4]] ->', transpose([[1, 2], [3, 4]]))
    print('[] ->', transpose([]))
    print('[[1, 2], [3]] ->', transpose([[1, 2], [3]]))
    # TEST row_sums
    print('[[1, 2, 3], [4, 5, 6]] ->', row_sums([[1, 2, 3], [4, 5, 6]]))
    print('[[-1, 1], [10, -10]] ->', row_sums([[-1, 1], [10, -10]]))
    print('[[0, 0], [0, 0]] ->', row_sums([[0, 0], [0, 0]]))
    print('[[1, 2], [3]] ->', row_sums([[1, 2], [3]]))
    # TEST col_sums
    print('[[1, 2, 3], [4, 5, 6]] ->', col_sums([[1, 2, 3], [4, 5, 6]]))
    print('[[-1, 1], [10, -10]] ->', col_sums([[-1, 1], [10, -10]]))
    print('[[0, 0], [0, 0]] ->', col_sums([[0, 0], [0, 0]]))
    print('[[1, 2], [3]] ->', col_sums([[1, 2], [3]]))