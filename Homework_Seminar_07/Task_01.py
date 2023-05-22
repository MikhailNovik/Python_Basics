# Задача 1. Создайте пользовательский аналог метода map().

def our_map(func, lst):
    return (func(elem) for elem in lst)
 
numbers = [1, 14, 6, 10, 3, 2, 5]
print(list(our_map(lambda x: x + 3, numbers)))
