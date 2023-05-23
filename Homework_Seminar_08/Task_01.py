# Задача 1. Напишите бота для техподдержки. 
# Бот должен записывать обращения пользователей в файл.
import telebot

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                f'Привет, я - Telegram Bot техподдержки.\n'
                f'Напишите сообщение команде техподдержки')


@bot.message_handler(content_types=['text'])
def text_message(message):
    try:
        f = open('log.txt', mode='a', encoding='utf-8')
    
    except Exception as e:
        bot.reply_to(message, str(e))
    else:
        with f:
            text = f'{message.message_id} : {message.from_user.id} : {message.text}\n'
            f.write(text)

bot.polling()
