# Задача 1. Дан список элементов. 
# Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

size = int(input('Введите длину списка: '))
numbers = np.random.randint(0, 10, size)
print(f'Список: {numbers}')

np_array = np.unique(numbers)
print(f'Количество уникальных элементов в списке: {len(np_array)}')
