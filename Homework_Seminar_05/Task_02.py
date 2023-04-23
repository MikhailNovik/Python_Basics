# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
import random

# Первый вариант решения
numbers = [1, 5, 2, 3, 4, 6, 1, 7]
print(f'Список случайных чисел: {numbers}')

for i in range(0, len(numbers) - 1):
    random_increasing_seq = [numbers[i]]
    for j in range(i + 1, len(numbers)):
        if numbers[j] > random_increasing_seq[-1]:
            random_increasing_seq.append(numbers[j])
    
    if len(random_increasing_seq) > 1:
        print(f'Cлучайная возрастающая последовательность: {random_increasing_seq}')
print()

# Второй вариант решения
numbers = [1, 5, 2, 3, 4, 6, 1, 7]
print(f'Список случайных чисел: {numbers}')
flag = True

while flag:
    start_index = random.randint(0, len(numbers) - 2)
    stop_index = random.randint(start_index + 1, len(numbers) - 1)
    random_seq = numbers[start_index: stop_index + 1]
    step = random.randint(1, len(random_seq) - 1)
    
    random_increasing_seq = [random_seq[0]]
    
    for i in range(0 + step, len(random_seq), step):
        if random_seq[i] > random_increasing_seq[-1]:
            random_increasing_seq.append(random_seq[i])

    if len(random_increasing_seq) > 1:
        flag = False

print(f'Cлучайная возрастающая последовательность: {random_increasing_seq}')
