import openai
import telebot
from telebot import types
import wikipedia
# Ключ для телеграмм бота
bot = telebot.TeleBot("key")
# Ключ для OpenAI и их приложений
openai.api_key = ("key")
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("📶Войти в сеть🌐")
    # btn2 = types.KeyboardButton('🌃"Техноград"🌊')
    # markup.add(btn1, btn2)
    btn3 = types.KeyboardButton('🤖Покупки в Технограде❗️')
    btn4 = types.KeyboardButton('🌃Хроники🌊')
    markup.add(btn3, btn4)
    bot.send_message(message.from_user.id,
                     '🌃🌔💎"ХРОНИКИ \nТЕХНОГРАДА" 🆕🌊💡'
                     "Привет, уважаемые слушатели Хроники Технограда! Мы рады Вам представить наш канал, "
                     "посвященный технологиям, инновациям и интересным историям из мира технологий. "
                     "Мы разбираемся в самых последних технологических трендах, "
                     "а также делимся нашими исследованиями и инсайтами. "
                     "Следите за нами и получайте последние новости из мира технологий и инноваций. "
                     "Добро пожаловать в Хроники Технограда!",
                     reply_markup=markup)


# Функция, обрабатывающая команду /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Пользуйтесь кнопкой МЕНЮ:"
                                           "\nstart - для начала и возврата в главное меню▶️,"
                                           "\nwiki - найди информацию на Википедии⚛️,"
                                           "\ndavinci - задай вопрос ИИ🤖"
                                           "\nдля каждого нового запроса к боту или ИИ")


# Подключаю команду davinci - она отвечает на вопросы как ИИ
@bot.message_handler(commands=['davinci'])
def davinci(message):
    bot.send_message(message.chat.id, "Пожалуйста, напишите сообщение:")
    bot.register_next_step_handler(message, get_davinci_text)


# создаем обработчик сообщений
def get_davinci_text(message):
    bot.reply_to(message, "Запрос принят в работу.")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text,
            max_tokens=3500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        bot.reply_to(message, response.choices[0].text)
    except:
        bot.reply_to(message, "Произошла ошибка при обработке вашего запроса.")


# Функция, обрабатывающая текст пользователя
@bot.message_handler(content_types=['text'])
def get_menu(message):

    if message.text == '🤖Покупки в Технограде❗️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton("📲Телефоны📱")
        btn2 = types.InlineKeyboardButton("⌚️Аксессуары🕶")
        markup.row(btn1, btn2)
        bot.reply_to(message,
                     "Добро пожаловать в магазин технологий будущего Марата! "
                     "Мы предлагаем большой выбор инновационных телефонов от ведущих мировых производителей."
                     "У нас вы найдете самые ходовые модели, созданные с использованием последних технологических достижений."
                     "Наша команда экспертов всегда готова проконсультировать вас по любому вопросу и помочь выбрать телефон,"
                     "отвечающий вашим потребностям. В нашем магазине вы также можете приобрести различное дополнительное оборудование,"
                     "такое как наушники, чехлы и другие аксессуары, для еще более комфортного использования вашего телефона."
                     "У нас вы найдете только самые высококачественные товары по приемлемым ценам."
                     "Приходите в наш магазин и окунитесь в мир будущего технологий!\n "
                         '\nПолный текст можно прочитать по ' + '[ссылке](https://t.me/msk77pro)', reply_markup=markup)
        bot.reply_to(message, "Какой товар хотите приобрести ?")
        # Переход к функции
        bot.register_next_step_handler(message, get_info_shop)

    elif message.text == '🌃Хроники🌊':
        bot.send_message(message.from_user.id,
                         '"Москва 2077: Хроники технограда" - это издание, посвященное жизни и событиям в технологическом мегаполисе Москва-2077. '
                         'Ее страницы наполнены новостями о самых современных технологиях, гиперсвязи, искусственном интеллекта, кибернетике и других научных достижениях, '
                         'которые перестали быть фантазиями ! ' + '[ссылке](https://dzen.ru/id/607fc499a17092441460fe48/)',
                         parse_mode='Markdown')

    else:
        bot.send_message(message.from_user.id, "Попытка не удачна, вернитесь в меню командой /start")


def get_info_shop(message):
    if message.text == "📲Телефоны📱":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Apple")
        markup.row(btn1)
        btn2 = types.KeyboardButton("Xiaomi")
        btn3 = types.KeyboardButton("Samsung")
        btn4 = types.KeyboardButton("Realme")
        markup.row(btn2, btn3, btn4)
        bot.reply_to(message, "Какой телефон хотите ?", reply_markup=markup)
        bot.register_next_step_handler(message, show_phone_models)

    elif message.text == "⌚️Аксессуары🕶":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Часы⌚️")
        btn2 = types.KeyboardButton("Очки🕶")
        btn3 = types.KeyboardButton("Наушники🎧")
        markup.row(btn1, btn2, btn3)
        bot.reply_to(message, " Что хотите из аксессуаров ?", reply_markup=markup)
        bot.register_next_step_handler(message, show_accessories_models)


# Функция просмотра моделей телефонов
def show_phone_models(message):
    if message.text == "Apple":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Apple, выбери ", reply_markup=markup)

    elif message.text == "Xiaomi":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Xiaomi", reply_markup=markup)

    elif message.text == "Samsung":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Samsung", reply_markup=markup)

    elif message.text == "Realme":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Realme", reply_markup=markup)


def show_accessories_models(message):
    if message.text == "Часы⌚️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Часы⌚️, выбери модель", reply_markup=markup)

    elif message.text == "Очки🕶":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Очки🕶, выбери модель", reply_markup=markup)

    elif message.text == "Наушники🎧":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Модель 1")
        btn2 = types.KeyboardButton("Модель 2")
        btn3 = types.KeyboardButton("Модель 3")
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ты выбрал(а) Наушники🎧, выбери модель", reply_markup=markup)


# Запускаем бота
if __name__ == "__main__":
    # bot.polling()
    bot.polling(none_stop=True, interval=0)
