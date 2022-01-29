import telebot
import config
import getdem

# что бы подкгрузить зависимости импортов нужно выполнить в терминале в ide
# pip install pyTelegramBotAPI


bot = telebot.TeleBot(config.token)
bot_info = bot.get_me()
bot_link = f"https://t.me/" + bot_info.username


def isadmin(chatid):
    if config.idadmin == chatid:
        return True
    else:
        return False


@bot.message_handler(commands=['what'])
def send_what(message):
    bot.send_message(message.chat.id, 'Сам создал проблему сам и расхлебывай!')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Помощь в пути!')
    bot.send_photo(message.chat.id, "https://cdn1.ozone.ru/s3/multimedia-r/c1200/6061237143.jpg")


@bot.message_handler(commands=['getdemot'])
def send_getdemot(message):
    if isadmin(message.chat.id):
        bot.send_photo(message.chat.id, getdem.get_random())


@bot.message_handler(commands=['start'])
def start(message):
    if message is not None:
        user = message.from_user.to_dict()
        user_id = user["id"]
        is_blocked_bot = False
        name = user["username"]
    if isadmin(message.chat.id):
        print(f"Админ в чате:{name} + {user_id}")
    else:
        print(f"Пользователь в чате: {name} + {user_id}")

    markup_inline = telebot.types.InlineKeyboardMarkup(row_width=3)
    key_1 = telebot.types.InlineKeyboardButton("У меня проблема", callback_data='what')
    key_2 = telebot.types.InlineKeyboardButton("Демотиватор дня", callback_data='getdemot')
    key_3 = telebot.types.InlineKeyboardButton("Помощь", callback_data='help')
    markup_inline.add(key_1, key_2, key_3)
    bot.send_message(message.chat.id, 'Ну что начнем!', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def logic_case(call):
    if call.data == 'help':
        send_help(call.message)

    if call.data == 'getdemot':
        send_getdemot(call.message)

    if call.data == 'what':
        send_what(call.message)


# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):  # Название функции не играет никакой роли


print(f"Pooling of '{bot_link}' started")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
