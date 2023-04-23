# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.

import random

length = int(input('Введите длину списка: '))
numbers = [random.randint(1, 10) for _ in range(length)]
print(f'Исходный список случайных чисел:{numbers}')

numbers = list(filter(lambda x: x > 5, numbers))
print(f'Список, который содержит элементы больше 5 из исходного списка:\n{numbers}')
