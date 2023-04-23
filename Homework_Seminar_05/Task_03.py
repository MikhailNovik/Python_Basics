# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

import random

# Первый вариант решения
length = int(input('Введите длину списка: '))
numbers = [random.randint(1, 10) for _ in range(length)]
print(f'Исходный список случайных чисел: {numbers}')

num = list(set(numbers))
print(f'Список уникальных элементов: {num}')
count = len(numbers) - len(num)
print(f'Количество совпадающих элементов в исходном списке: {count}')
print()

# Второй вариант решения
print(f'Исходный список случайных чисел: {numbers}')
print(f'Список уникальных элементов: {num}')
count = [numbers.count(i) > 1 for i in num].count(True)
print(f'Количество совпадающих элементов в исходном списке: {count}')

