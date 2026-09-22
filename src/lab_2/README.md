Лабораторная работа № 2

Задача № 1 
```python
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
```
![Вывод min_max](images/lab_2/img_01.png)

```python
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
```

```python
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
```
