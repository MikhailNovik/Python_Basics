"""
Задача 2. Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.
"""

import math

x_first_point = float(input('Введите координату по оси x первой точки: '))
y_first_point = float(input('Введите координату по оси y первой точки: '))
x_second_point = float(input('Введите координату по оси x второй точки: '))
y_second_point = float(input('Введите координату по оси y второй точки: '))

distance = math.sqrt(((x_second_point - x_first_point) ** 2) + ((y_second_point - y_first_point) ** 2))

print(f'Расстояние между двумя точками в 2D пространстве равно {distance}')
