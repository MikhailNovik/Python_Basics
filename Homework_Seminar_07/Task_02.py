# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
def repeat(count):
    def wrap_func(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return wrap_func


count = int(input('Введите необходимое количество вызовов функции: '))

@repeat(count)
def greeting(name):
    print(f'Привет, {name}!')


greeting('Tom')