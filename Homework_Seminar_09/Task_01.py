# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

size = (4, 4)
numbers = np.random.randint(0, 4, size)
print(numbers)
print(np.diag(numbers))
result = numbers.any(axis=0)
print(result)
result = ~result
print(result)

if True in result:
    print(f'В матрице есть столбец, состоящий из нулей')
else:
     print(f'В матрице нет столбца, состоящего из нулей')


# user = input(f'Введите \n'
#              f'()\n'
#              f'или введите "cтоп" для завершения программы\n'
#              f': ').lower()

# n = [random.randint(0, 10) for el in range(length)]
# p = ''.join([string[random.randint(0, len(string) - 1)] for _ in range(length)])

# print(f'{=}')
# print(f'{=} {}')
