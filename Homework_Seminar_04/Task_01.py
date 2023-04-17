# Задача 1. Дано натуральное число N. 
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

def calc_prime_factorization(number):
    prime_factors = []
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    
    if number > 1:
        prime_factors.append(number)
    
    count = len(prime_factors)
    
    return prime_factors, count

N = int(input('Введите натуральное число: '))

prime_factors, count = calc_prime_factorization(N)
print(f'Cписок простых множителей числа {N}: {prime_factors}')
print(f'Количество простых множителей числа {N}: {count}')
