"""
Задача 3. Напишите программу, которая по заданному номеру четверти,
 показывает диапазон возможных координат точек в этой четверти (х и у).
"""
num = int(input('Введите номер координатной четверти: '))

if num == 1:
    print(f'Диапазон возможных координат точек в {num}-й четверти: x > 0, y > 0')
elif num == 2:
    print(f'Диапазон возможных координат точек в {num}-й четверти: x < 0, y > 0')
elif num == 3:
    print(f'Диапазон возможных координат точек в {num}-й четверти: x < 0, y < 0')
elif num == 4:
     print(f'Диапазон возможных координат точек в {num}-й четверти: x > 0, y < 0')
else:
    print('Такой координатной четверти не существует')

    