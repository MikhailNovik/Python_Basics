# Задача 2. Создайте двумерный массив, размером 5х5. 
# Определите, есть ли в нём одинаковые строки.

import numpy as np

size = (5, 5)
matrix = np.random.randint(0, 3, size)
print(f'Двумерный массив, размером 5х5:\n{matrix}')
result = np.corrcoef(matrix)
print(result)

for row in result:
    if [True for num in row if num == 1].count(True) >= 2:
        print('В двумерном массиве есть одинаковые строки')
        break
else:
    print('В двумерном массиве нет одинаковых строк')
