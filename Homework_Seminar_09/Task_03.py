# Задача 3. Создайте двумерный массив случайного размера.
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

size = int(input('Введите размер двумерного массива: '))
size = (size, size)
numbers = np.random.randint(0, 10, size)
print(f'Двумерный массив:\n{numbers}')

ind_max_elem = np.argmax(numbers)
ind_min_elem = np.argmin(numbers)

print(f'Индекс максимального элемента в матрице: {ind_max_elem}')
print(f'Индекс минимального элемента в матрице: {ind_min_elem}')
print(f'Элементы главной диагонали матрицы:\n {np.diag(numbers)}')
