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
    minimum = maximum = nums[0]
    for x in nums[1:]:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Параметры:
        nums: список чисел.

    Возвращает:
        Отсортированный список уникальных значений по возрастанию.
    """
    unique_nums = list(set(nums))
    for i in range(1, len(unique_nums)):
        key = unique_nums[i] # элемент, который хотим вставить
        j = i - 1 # индекс последнего отсортированого элемента
        while j >= 0 and unique_nums[j] > key: # если элемент > key, сдвигаем вправо
            unique_nums[j + 1] = unique_nums[j]
            j -= 1
        unique_nums[j + 1] = key # вставляем нужный элемент в освободившееся место
    return unique_nums


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
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Встретился элемент, который не является списком/кортежем")
        for item in row:
            row_major.append(item)
    return row_major
    
if __name__ == "__main__":
    # TEST min_max
    '''print('[3, -1, 5, 5, 0] ->', min_max([3, -1, 5, 5, 0]))
    print('[42] ->', min_max([42]))
    print('[-5, -2, -9] ->', min_max([-5, -2, -9]))
    print('[1.5, 2, 2.0, -3.1] ->', min_max([1.5, 2, 2.0, -3.1]))
    print('[] ->', min_max([]))
    # TEST unique_sorted
    print('[3, 1, 2, 1, 3] ->', unique_sorted([3, 1, 2, 1, 3]))
    print('[] ->', unique_sorted([]))
    print('[-1, -1, 0, 2, 2] ->', unique_sorted([-1, -1, 0, 2, 2]))
    print('[1.0, 1, 2.5, 2.5, 0] ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))
    '''# TEST flatten
    print('[[1, 2], [3, 4]] ->', flatten([[1, 2], [3, 4]]))
    print('[[1, 2], (3, 4, 5)] ->', flatten([[1, 2], (3, 4, 5)]))
    print('[[1], [], [2, 3]]->', flatten([[1], [], [2, 3]]))
    print('[[1, 2], "ab"] ->', flatten([[1, 2], "ab"]))
