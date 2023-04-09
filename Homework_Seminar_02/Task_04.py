# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

N = int(input('Введите кол-во элементов в списке: '))
original_list = []
original_list = list(range(-N, N + 1))
length = len(original_list)
print(f'Исходный список: {original_list}\n')

shift = 2
shifted_list = []
for i in range(length):
    shifted_list.append(original_list[i - shift])

print(f'Cписок элементы, которого сдвинуты относительно исходного на 2 позиции вправо:\n{shifted_list}')