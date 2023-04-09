# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй.

phrase_1 = input('Введите первую строку: ')
phrase_2 = input('Введите вторую строку: ')
length_phrase_1 = len(phrase_1)
length_phrase_2 = len(phrase_2)
unique_symbol_phrase_1 = []

for symbol in phrase_1:
    if symbol not in unique_symbol_phrase_1:
        unique_symbol_phrase_1.append(symbol)

for symbol in unique_symbol_phrase_1:
    сount_symbol = 0
    for sym in phrase_2:
        if symbol == sym:
            сount_symbol += 1
    print(f'Символ "{symbol}" из первой строки во второй строке встречается {сount_symbol} раз(-а)')
