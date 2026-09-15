def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Параметры:
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
    """Параметры:
        nums: список чисел.

    Возвращает:
        Отсортированный список уникальных значений по возрастанию.
    """
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    """Параметры:
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


# ---------------------------------------------------------
# ЭТОТ БЛОК НУЖЕН, ЧТОБЫ ФУНКЦИИ ЗАПУСТИЛИСЬ И ВСЁ ПРОВЕРИЛОСЬ
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=== Проверка min_max ===")
    tests_min_max = [
        ([3, -1, 5, 5, 0], (-1, 5)),
        ([42], (42, 42)),
        ([-5, -2, -9], (-9, -2)),
        ([1.5, 2, 2.0, -3.1], (-3.1, 2)),
    ]
    for i, (inp, expected) in enumerate(tests_min_max, 1):
        result = min_max(inp)
        status = "✅" if result == expected else "❌"
        print(f"Тест {i}: {status} | min_max({inp}) → {result} (ожидалось {expected})")

    # Проверка ошибки на пустом списке
    try:
        min_max([])
        print("Тест min_max([]): ❌ | Должен был выбросить ошибку!")
    except ValueError:
        print("Тест min_max([]): ✅ | Правильно выброшен ValueError")


    print("\n=== Проверка unique_sorted ===")
    tests_unique = [
        ([3, 1, 2, 1, 3], [1, 2, 3]),
        ([], []),
        ([-1, -1, 0, 2, 2], [-1, 0, 2]),
        ([1.0, 1, 2.5, 2.5, 0], [0, 1.0, 2.5]),
    ]
    for i, (inp, expected) in enumerate(tests_unique, 1):
        result = unique_sorted(inp)
        status = "✅" if result == expected else "❌"
        print(f"Тест {i}: {status} | unique_sorted({inp}) → {result} (ожидалось {expected})")


    print("\n=== Проверка flatten ===")
    tests_flatten = [
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1, 2], (3, 4, 5)], [1, 2, 3, 4, 5]),
        ([[1], [], [2, 3]], [1, 2, 3]),
    ]
    for i, (inp, expected) in enumerate(tests_flatten, 1):
        result = flatten(inp)
        status = "✅" if result == expected else "❌"
        print(f"Тест {i}: {status} | flatten({inp}) → {result} (ожидалось {expected})")

    # Проверка ошибки на неверном типе
    try:
        flatten([[1, 2], "ab"])
        print("Тест flatten([[1,2], 'ab']): ❌ | Должен был выбросить ошибку!")
    except TypeError:
        print("Тест flatten([[1,2], 'ab']): ✅ | Правильно выброшен TypeError")

    print("\n🎉 Все проверки завершены!")
