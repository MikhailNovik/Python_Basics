# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.
import telebot

token = ''
bot = telebot.TeleBot(token)

with open('log.txt', mode='r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        message_id, user_id, user_question = line.strip().split(' : ')
        answer = input('Введите ответ на вопрос пользователя: ')
        bot.send_message(user_id, f'Ответ техподдержки: {answer}',
                         reply_to_message_id=message_id)
