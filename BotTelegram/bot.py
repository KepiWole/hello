import telebot
from telebot import types # для указание типов
import Config

bot = telebot.TeleBot(Config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📝 Информация")
    item2 = types.KeyboardButton("Оксфордский опросник счастья")
    item3 = types.KeyboardButton("Жизнестойкость Мадди")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text='Привет, {0.first_name}!'
                                             '\nДанный бот содержит два Психологических теста, которые можно пройти,и сразу'
                                             'получить результат! Больше информации можно получить в разделе \"Информация\"'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "📝 Информация":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item4 = types.KeyboardButton("Оксфордский опросник cчастья") # c in eng
        item5 = types.KeyboardButton("Жизнеcтойкость Мадди") # too eng
        item6 = types.KeyboardButton("В главное меню")
        markup.add(item4, item5, item6)
        bot.send_message(message.chat.id, text='Выберите тест о котором хотели бы узнать.', reply_markup=markup)
    elif message.text == "Жизнеcтойкость Мадди":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6 = types.KeyboardButton("Вернуться в раздел \"📝 Информация\"")
        item7 = types.KeyboardButton("В главное меню")
        markup.add(item6, item7)
        bot.send_message(message.chat.id, text='Тест жизнестойкости Мадди.\nТест жизнестойкости (Hardiness Survey) разработан в '
                                                 'рамках изучения факторов, способствующих успешному '
                                                 'совладанию со стрессом и снижению внутреннего напряжения. Жизнестойкость здесь определяется как некая '
                                                 'экзистенциальная отвага, позволяющая личности в '
                                                 'меньшей степени зависеть от ситуативных переживаний, преодолевать постоянную '
                                                 'базовую тревогу, актуализирующуюся в ситуации неопределённости и необходимости выбора.', reply_markup = markup)
    elif message.text == "Оксфордский опросник cчастья":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6 = types.KeyboardButton("Вернуться в раздел \"📝 Информация\"")
        item7 = types.KeyboardButton("В главное меню")
        markup.add(item6, item7)
        bot.send_message(message.chat.id, text='Оксфордский опросник счастья (Oxford Happiness Inventory, OHI) был разработан в конце 1980-х на кафедре '
                                                'экспериментальной психологии Оксфордского университета Майклом Аргайлом (Michael Argyle) с коллегами, изначально '
                                                'для проводившихся в Оксфорде исследований. Методика предназначена для измерения счастья в целом, и основывается на '
                                                'опроснике депрессии Бека, из которого заимствована часть вопросов. Результаты представляются в процентах.', reply_markup = markup)

    elif message.text == "В главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("📝 Информация")
        item2 = types.KeyboardButton("Оксфордский опросник счастья")
        item3 = types.KeyboardButton("Жизнестойкость Мадди")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню.", reply_markup=markup)
    elif message.text == "Вернуться в раздел \"📝 Информация\"":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item4 = types.KeyboardButton("Оксфордский опросник cчастья") # c in eng
        item5 = types.KeyboardButton("Жизнеcтойкость Мадди ") # too eng
        item6 = types.KeyboardButton("В главное меню")
        markup.add(item4, item5, item6)
        bot.send_message(message.chat.id, text='Вы вернулись в раздел \"Информация\"', reply_markup = markup)

bot.polling(none_stop=True)
