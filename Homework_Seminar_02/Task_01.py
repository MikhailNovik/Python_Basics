# Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.

N = int(input('Введите число: '))
numbers = list(range(1, N + 1))

factorials = []
for num in numbers:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    factorials.append(factorial)

print(f'Cписок факториалов для чисел от 1 до {N}: {factorials}')