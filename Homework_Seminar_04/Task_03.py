# Задача 3. Выведите число π с заданной точностью. 
# Точность вводится в виде десятичной дроби.

import math

user_float = input(f'Введите десятичную дробь с желаемым количеством разрядов после "."\n'
                  f'например: 0.01 -> желаемое количество разрядов после после "." => "2"\n'
                  f': ')

# count_after_decimal = user_float[::-1].find('.')
count_after_decimal = len(user_float.split('.')[1])

print(f'Число π с заданной точностью: {round(math.pi, count_after_decimal)}')
