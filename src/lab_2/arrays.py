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
# TEST min_max
'''print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))'''
'print(min_max([]))'
'''print(min_max([1.5, 2, 2.0, -3.1]))
# TEST unique_sorted
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
# TEST flatten
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))'''
print(flatten([[1, 2], "ab"]))
