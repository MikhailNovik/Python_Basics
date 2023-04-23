# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def find_GCD(a, b):
    if(b == 0):
        return a
    else:
        return find_GCD(b, a % b)

irreducible_fractions = []

for denominator in range(2, 12):
    for numerator in range(1, denominator):
        if find_GCD(numerator, denominator) == 1:
            irreducible_fractions.append(f'{numerator}/{denominator}')

print(f'Простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11:\n{irreducible_fractions}')
