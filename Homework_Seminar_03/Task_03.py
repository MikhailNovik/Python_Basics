# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.


bot_dictionary = {'привет': 'Здравствуй!\n', 'как тебя зовут?': 'Меня зовут, Анатолий\n', 'как дела?': 'Хорошо\n'}
flag = True

while flag:
    user_phrase = input(f'Поприветствуйте бота\n'
                        f'или введите вопрос, адресованный боту\n'
                        f'или введите "стоп" для завершения сеанса\n'
                        f': ').lower()
    
    if user_phrase == 'стоп':
        flag = False
        print('Сеанс завершен')
    else:
        print(bot_dictionary.get(user_phrase, 'У бота нет ответа на ваш вопрос'))
