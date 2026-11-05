def linear_search(nums, x) -> int:
    """Алгоритм линейного поиска.

    Возвращает индекс первого вхождения x или -1, если элемент не найден.
    """
    for i, num in enumerate(nums):
        if num == x:
            return i

    return -1

def binary_search(sorted_nums, x) -> int:
    """Алгоритм бинарного поиска.

    Возвращает индекс любого вхождения x или -1, если элемент не найден.

    На неотсортированном списке результат не определён.
    """
    low = 0
    high = len(sorted_nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_nums[mid]
        if guess == x:
            return mid
        elif guess > x:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """Ищет два числа с суммой target перебором пар.

    Возвращает кортеж (i, j) или None, если он не найден.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """Ищет два числа с суммой target за один проход через хэш-таблицу (словарь).

    Возвращает кортеж (i, j) или None, если он не найден.
    """
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i

    return None