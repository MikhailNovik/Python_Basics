# Задача 1. Дано натуральное число N. 
# Найдите значение выражения:N + NN + NNN
# N может быть любой длины.

N = input(f'Введите натуральное число: ')

expression = 'N + NN + NNN'
result = sum(map(int, expression.replace('N', N).split('+')))

print(f'Значение выражения: {result}')
