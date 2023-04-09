# Задача 2. Выведите таблицу истинности для выражения ¬(X ⋀ Y) ⋁ Z.

print(f'X | Y | Z   ¬(X ⋀ Y) ⋁ Z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'{x} | {y} | {z}\t {int(not(x and y) or z)}')
