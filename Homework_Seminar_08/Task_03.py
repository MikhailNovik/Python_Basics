import telebot
from telebot import types

bot = telebot.TeleBot("6216302751:AAGHbz4pORQaBOA3pDi8iDBIjVROrA_J3Rs")

markup = types.ReplyKeyboardMarkup(row_width=1)

itembtn1 = types.KeyboardButton('регистрация')
itembtn2 = types.KeyboardButton('оповещение')
markup.add(itembtn1, itembtn2)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Привет, я - Telegram Bot.\nДля справки нажмите /help', reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                    f'Cписок команд Telegram Botа:\n'
                    f'/регистрация\n'
                    f'/оповещение\n'
                    f'/start')

@bot.message_handler(content_types=['text'])
def text_message(message): 
    if message.text == 'регистрация':
        with open('registred_users.txt', mode='r+', encoding='utf-8') as f:
            id_list = f.read().split('\n')
            print(f'{id_list=}')
            user_id = str(message.from_user.id)
        if user_id not in id_list:
            with open('registred_users.txt', mode='a+', encoding='utf-8') as f:
                text = f'{user_id}\n'
                f.write(text)
                bot.reply_to(message, 'Регистрация прошла успешно.')
        else:
            bot.reply_to(message, 'Вы уже зарегистрированы.')
    
    elif message.text == 'оповещение':
        with open('registred_users.txt', mode='r+', encoding='utf-8') as f:
            id_list = f.read().split('\n')
            print(f'{id_list=}')
            id_list = id_list[:-1]
            print(f'{id_list=}')
            for id in id_list:
                bot.send_message(id, 'Совещание через 15 минут.')

    else:
        with open('log.txt', mode='a', encoding='utf-8') as f:
            text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
            f.write(text)    


bot.polling()
