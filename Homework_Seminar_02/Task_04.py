# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
N = int(input('Введите кол-во элементов в списке: '))
original_list = list(range(-N, N + 1))
print(f'Исходный список: {original_list}\n')

shift = 2
shifted_list = original_list[-shift:] + original_list[:-shift]
print(f'Список элементы, которого сдвинуты относительно исходного на {shift} позиции вправо:\n{shifted_list}')
