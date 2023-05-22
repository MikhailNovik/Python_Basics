# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.
import telebot
import requests
import random

bot = telebot.TeleBot("6216302751:AAGHbz4pORQaBOA3pDi8iDBIjVROrA_J3Rs")
storage = dict()


def init_storage(chat_id):
    storage[chat_id] = dict(bot_number=None, attempts=0)


def increase_number_attempts(chat_id):
    storage[chat_id]['attempts'] += 1


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, я - Telegram Bot.')
    bot.send_message(message.chat.id,
                    f'1.Если вы отправите мне сообщение "привет",\nя поприветствую Вас по имени.\n'
                    f'2.Если вы отправите мне сообщение "погода",\nя сообщу Вам текущую погоду.\n'
                    f'3.Если вы отправите мне сообщение "котик",\nя отправляю Вам random фото котика.\n'
                    f'4.Если вы отправите мне сообщение "угадай число",\nВы сможете сыграть со мной в игру "Угадай число".')

@bot.message_handler(content_types=['text'])
def greetings(message):
    try: 
        text = message.text.lower()
        if 'привет' in text:
            bot.reply_to(message, f'Привет, {message.from_user.first_name}.')
        elif 'погода' in text:
            req = requests.get('https://wttr.in/?0T')
            bot.reply_to(message, req.text)
        elif 'котик' in text:
            req = requests.get('https://cataas.com/cat')
            bot.send_photo(message.chat.id, req.content)
        elif 'угадай число' in text:
            msg = bot.send_message(message.chat.id,
                                   f'Запущена игра "Угадай число".\n'
                                   f'Бот загадал число. Попробуйте угадать.\n'
                                   f'Введите число от 1 до 1000')
            init_storage(message.chat.id)
            bot_choice = random.randint(1, 1000)
            storage[message.chat.id]['bot_number'] = bot_choice
            bot.register_next_step_handler(msg, game_guess_number)
    except Exception as e:
        bot.reply_to(message, str(e))


def game_guess_number(message):
    user_number = message.text
    if not user_number.isdigit():
        increase_number_attempts(message.chat.id)
        msg = bot.reply_to(message,
                           f'Бот загадал ЧИСЛО. Вам необходимо ввести ЧИСЛО.\n'
                           f'Введите число от 1 до 1000')
        bot.register_next_step_handler(msg, game_guess_number)
    else:
        if int(user_number) == storage[message.chat.id]['bot_number']:
            increase_number_attempts(message.chat.id)
            attempts = storage[message.chat.id]['attempts']
            msg = bot.send_message(message.chat.id,
                                   f'Вы угадали число с {attempts} попыток(и).\n'
                                   f'Победа!')
            bot.register_next_step_handler(msg, greetings)
        elif int(user_number) < storage[message.chat.id]['bot_number']:
            increase_number_attempts(message.chat.id)
            msg = bot.reply_to(message,
                               f'Число меньше, чем загаданное ботом.\n'
                               f'Попробуйте ещё раз!')
            bot.register_next_step_handler(msg, game_guess_number)
        else:
            increase_number_attempts(message.chat.id)
            msg = bot.reply_to(message,
                               f'Число больше, чем загаданное ботом.\n'
                               f'Попробуйте ещё раз!')
            bot.register_next_step_handler(msg, game_guess_number)


bot.polling()
