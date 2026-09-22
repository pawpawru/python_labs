def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Параметры:
        nums: список чисел.

    Возвращает:
        Кортеж из двух элементов: (минимум, максимум).

    Вызывает:
        ValueError: если список пуст.
    """
    if not nums:
        raise ValueError("Список пуст")
    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Параметры:
        nums: список чисел.

    Возвращает:
        Отсортированный список уникальных значений по возрастанию.
    """
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    """
    Параметры:
        mat: список списков/кортежей.

    Возвращает:
        Список, «расплющенный» по строкам (row-major).

    Вызывает:
        TypeError: если встретился элемент, не являющийся списком или кортежем.
    """
    row_major = []
    if not all(isinstance(i, (list, tuple)) for i in mat):
        raise TypeError("Встретился элемент, который не является списком/кортежем")
    else:
        for i in mat:
            for j in i:
                row_major.append(j)
        return row_major
    
if __name__ == "__main__":
    # TEST min_max
    '''print('[3, -1, 5, 5, 0] ->', min_max([3, -1, 5, 5, 0]))
    print('[42] ->', min_max([42]))
    print('[-5, -2, -9] ->', min_max([-5, -2, -9]))
    print('[] ->', min_max([]))
    print('[1.5, 2, 2.0, -3.1] ->', min_max([1.5, 2, 2.0, -3.1]))
    # TEST unique_sorted
    print('[3, 1, 2, 1, 3] ->', unique_sorted([3, 1, 2, 1, 3]))
    print('[] ->', unique_sorted([]))
    print('[-1, -1, 0, 2, 2] ->', unique_sorted([-1, -1, 0, 2, 2]))
    print('[1.0, 1, 2.5, 2.5, 0] ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))'''
    # TEST flatten
    print('[[1, 2], [3, 4]] ->', flatten([[1, 2], [3, 4]]))
    print('[[1, 2], (3, 4, 5)] ->', flatten([[1, 2], (3, 4, 5)]))
    print('[[1], [], [2, 3]]->', flatten([[1], [], [2, 3]]))
    print('[[1, 2], "ab"] ->', flatten([[1, 2], "ab"]))
