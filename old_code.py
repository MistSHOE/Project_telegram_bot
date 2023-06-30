#Бывший файл Telegram_bot.py 11.06.2023
# import openai
# import telebot
# from telebot import types
# import wiki_modul
#
# bot = telebot.TeleBot("key")
# openai.api_key = "key"
#
#
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("📶Войти в сеть🌐")
#     btn2 = types.KeyboardButton('🌃"Техноград"🌊')
#     btn3 = types.KeyboardButton("💎💡 Идея 💡💎")
#     btn4 = types.KeyboardButton('👋Вопрос❗️❓🤖')
#     markup.add(btn1, btn2, btn3, btn4)
#     bot.send_message(message.from_user.id, '🌃🌔💎"ХРОНИКИ \nТЕХНОГРАДА" 🆕🌊💡', reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     # Первая кнопка, функционал: Магазин и Новости
#     if message.text == '📶Войти в сеть🌐':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
#         btn1 = types.KeyboardButton('🤖Покупки в Технограде❗️')
#         btn2 = types.KeyboardButton('🌃Хроники🌊')
#         markup.add(btn1, btn2)
#         bot.send_message(message.from_user.id, 'Лавка: 🤖Покупки в Технограде❗️ \nПрочитать новости: 🌃Хроники🌊 ',
#                          reply_markup=markup)  # ответ бота
#
#     elif message.text == '🤖Покупки в Технограде❗️':
#         bot.send_message(message.from_user.id,
#                          "Добро пожаловать в магазин технологий будущего Марата! "
#                          "Мы предлагаем большой выбор инновационных телефонов от ведущих мировых производителей."
#                          "У нас вы найдете самые ходовые модели, созданные с использованием последних технологических достижений."
#                          "Наша команда экспертов всегда готова проконсультировать вас по любому вопросу и помочь выбрать телефон,"
#                          "отвечающий вашим потребностям. В нашем магазине вы также можете приобрести различное дополнительное оборудование,"
#                          "такое как наушники, чехлы и другие аксессуары, для еще более комфортного использования вашего телефона."
#                          "У нас вы найдете только самые высококачественные товары по приемлемым ценам."
#                          "Приходите в наш магазин и окунитесь в мир будущего технологий!\n "
#                          '\nПолный текст можно прочитать по ' + '[ссылке](https://t.me/msk77pro)',
#                          parse_mode='Markdown')
#
#     elif message.text == '🌃Хроники🌊':
#         bot.send_message(message.from_user.id,
#                          '"Москва 2077: Хроники технограда" - это издание, посвященное жизни и событиям в технологическом мегаполисе Москва-2077. '
#                          'Ее страницы наполнены новостями о самых современных технологиях, гиперсвязи, искусственном интеллекта, кибернетике и других научных достижениях, '
#                          'которые перестали быть фантазиями ! ' + '[ссылке](https://dzen.ru/id/607fc499a17092441460fe48/)',
#                          parse_mode='Markdown')
#
#     # Вторая кнопка, функционал: Чат с ии, ответы с Википедии
#     elif message.text == '🌃"Техноград"🌊':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
#         btn1 = types.KeyboardButton('🤖Общение с ИИ❗️')
#         btn2 = types.KeyboardButton('🌃Хроники Wiki🌊')
#         markup.add(btn1, btn2)
#         bot.send_message(message.from_user.id, '🤖Общение с ИИ❗\n🌃Хроники Wiki🌊 ', reply_markup=markup)  # ответ бота
#     #
#     # elif message.text == '🌃Хроники Wiki🌊':
#     #     bot.send_message(message.from_user.id, "Вы написали: ")
#
#
# # bot.polling(none_stop=True, interval=0)
# if __name__ == "__main__":
#     bot.polling()


# # Функция, обрабатывающая команду /wiki
# @bot.message_handler(commands=["wiki"])
# def wiki(message):
#     send = bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
#     bot.register_next_step_handler(send, get_message_wiki)


# def get_message_wiki(message):
#     bot.send_message(message.chat.id, getwiki(message.text))
#
#
# # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext=ny.content[:1000]
#         # Разделяем по точкам
#         wikimas=wikitext.split('.')
#         # Отбрасываем всЕ после последней точки
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
#         for x in wikimas:
#             if not('==' in x):
#                 # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'


# # Функция, обрабатывающая команду /help
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.from_user.id, "Пользуйтесь кнопкой МЕНЮ:"
#                                            "start - для начала и возврата в главное меню▶️,"
#                                            "wiki - найди информацию на Википедии⚛️,"
#                                            "davinci - задай вопрос ИИ🤖"
#                                            "для каждого нового запроса к боту или ИИ")
#
#
# # Функция, обрабатывающая команду /wiki
# @bot.message_handler(commands=["wiki"])
# def wiki(message):
#     send = bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
#     bot.register_next_step_handler(send, get_message_wiki)
#
#
# def get_message_wiki(message):
#     bot.send_message(message.chat.id, getwiki(message.text))
#
#
# # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext=ny.content[:1000]
#         # Разделяем по точкам
#         wikimas=wikitext.split('.')
#         # Отбрасываем всЕ после последней точки
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
#         for x in wikimas:
#             if not('==' in x):
#                 # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'
#
#
# # Подключаю команду davinci - она отвечает на вопросы как ИИ
# @bot.message_handler(commands=['davinci'])
# def davinci(message):
#     bot.send_message(message.chat.id, "Пожалуйста, напишите сообщение:")
#     bot.register_next_step_handler(message, get_davinci_text)
#
#
# # создаем обработчик сообщений
# def get_davinci_text(message):
#     bot.reply_to(message, "Запрос принят в работу.")
#     try:
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=message.text,
#             max_tokens=3500,
#             n=1,
#             stop=None,
#             temperature=0.5,
#         )
#         bot.reply_to(message, response.choices[0].text)
#     except:
#         bot.reply_to(message, "Произошла ошибка при обработке вашего запроса.")
#
#
# # Функция, обрабатывающая текст пользователя
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     # Первая кнопка, функционал: Магазин и Новости
#     if message.text == '📶Войти в сеть🌐':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
#         btn1 = types.KeyboardButton('🤖Покупки в Технограде❗️')
#         btn2 = types.KeyboardButton('🌃Хроники🌊')
#         markup.add(btn1, btn2)
#         bot.send_message(message.from_user.id, 'Лавка: 🤖Покупки в Технограде❗️ \nПрочитать новости: 🌃Хроники🌊 ',
#                          reply_markup=markup)  # ответ бота
#
#     elif message.text == '🤖Покупки в Технограде❗️':
#         bot.send_message(message.from_user.id,
#                          "Добро пожаловать в магазин технологий будущего Марата! "
#                          "Мы предлагаем большой выбор инновационных телефонов от ведущих мировых производителей."
#                          "У нас вы найдете самые ходовые модели, созданные с использованием последних технологических достижений."
#                          "Наша команда экспертов всегда готова проконсультировать вас по любому вопросу и помочь выбрать телефон,"
#                          "отвечающий вашим потребностям. В нашем магазине вы также можете приобрести различное дополнительное оборудование,"
#                          "такое как наушники, чехлы и другие аксессуары, для еще более комфортного использования вашего телефона."
#                          "У нас вы найдете только самые высококачественные товары по приемлемым ценам."
#                          "Приходите в наш магазин и окунитесь в мир будущего технологий!\n "
#                          '\nПолный текст можно прочитать по ' + '[ссылке](https://t.me/msk77pro)',
#                          parse_mode='Markdown')
#
#     elif message.text == '🌃Хроники🌊':
#         bot.send_message(message.from_user.id,
#                          '"Москва 2077: Хроники технограда" - это издание, посвященное жизни и событиям в технологическом мегаполисе Москва-2077. '
#                          'Ее страницы наполнены новостями о самых современных технологиях, гиперсвязи, искусственном интеллекта, кибернетике и других научных достижениях, '
#                          'которые перестали быть фантазиями ! ' + '[ссылке](https://dzen.ru/id/607fc499a17092441460fe48/)',
#                          parse_mode='Markdown')
#
#     else:
#         bot.send_message(message.from_user.id, "Попытка не удачна")
#
#
# # Запускаем бота
# if __name__ == "__main__":
#     # bot.polling()
#     bot.polling(none_stop=True, interval=0)


# if message.text == '🤖Покупки в Технограде❗️':
#     # Первая кнопка, функционал: Магазин и Новости
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
#     btn1 = types.KeyboardButton("Apple")
#     btn2 = types.KeyboardButton("Xiaomi")
#     btn3 = types.KeyboardButton("Samsung")
#     btn4 = types.KeyboardButton("Realme")
#     markup.add(btn1, btn2, btn3, btn4)
#     bot.send_message(message.from_user.id, 'Лавка: 🤖Покупки в Технограде❗️ \nПрочитать новости: 🌃Хроники🌊 ',
#                      reply_markup=markup)  # ответ бота
#
# elif message.text == '🌃"Техноград"🌊':
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton("📲Телефоны📱")
#     btn2 = types.InlineKeyboardButton("⌚️Аксессуары🕶")
#     bot.send_message(message.from_user.id,
#                      "Добро пожаловать в магазин технологий будущего Марата! "
#                      "Мы предлагаем большой выбор инновационных телефонов от ведущих мировых производителей."
#                      "У нас вы найдете самые ходовые модели, созданные с использованием последних технологических достижений."
#                      "Наша команда экспертов всегда готова проконсультировать вас по любому вопросу и помочь выбрать телефон,"
#                      "отвечающий вашим потребностям. В нашем магазине вы также можете приобрести различное дополнительное оборудование,"
#                      "такое как наушники, чехлы и другие аксессуары, для еще более комфортного использования вашего телефона."
#                      "У нас вы найдете только самые высококачественные товары по приемлемым ценам."
#                      "Приходите в наш магазин и окунитесь в мир будущего технологий!\n "
#                      '\nПолный текст можно прочитать по ' + '[ссылке](https://t.me/msk77pro)',
#                      parse_mode='Markdown')
#
#
#
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("📶Войти в сеть🌐")
#     btn2 = types.KeyboardButton('🌃Техноград🌊')
#     markup.add(btn1, btn2)
#     bot.send_message(message.from_user.id, '🌃🌔💎"ХРОНИКИ \nТЕХНОГРАДА" 🆕🌊💡'
#                      "Привет, уважаемые слушатели Хроники Технограда! Мы рады Вам представить наш канал, посвященный технологиям, инновациям и интересным историям из мира технологий. Мы разбираемся в самых последних технологических трендах, а также делимся нашими исследованиями и инсайтами. Следите за нами и получайте последние новости из мира технологий и инноваций. Добро пожаловать в Хроники Технограда!",
#                      reply_markup=markup)
#
#
# # Функция, обрабатывающая команду /help
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.from_user.id, "Пользуйтесь кнопкой МЕНЮ:"
#                                            "\nstart - для начала и возврата в главное меню▶️,"
#                                            "\nwiki - найди информацию на Википедии⚛️,"
#                                            "\ndavinci - задай вопрос ИИ🤖"
#                                            "\nдля каждого нового запроса к боту или ИИ")
#
#
# # Подключаю команду davinci - она отвечает на вопросы как ИИ
# @bot.message_handler(commands=['davinci'])
# def davinci(message):
#     bot.send_message(message.chat.id, "Пожалуйста, напишите сообщение:")
#     bot.register_next_step_handler(message, get_davinci_text)
#
#
# # создаем обработчик сообщений
# def get_davinci_text(message):
#     bot.reply_to(message, "Запрос принят в работу.")
#     try:
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=message.text,
#             max_tokens=3500,
#             n=1,
#             stop=None,
#             temperature=0.5,
#         )
#         bot.reply_to(message, response.choices[0].text)
#     except:
#         bot.reply_to(message, "Произошла ошибка при обработке вашего запроса.")
#
#
# # Функция, обрабатывающая текст пользователя
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     # Первая кнопка, функционал: Магазин и Новости
#     if message.text == '📶Войти в сеть🌐':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
#         btn1 = types.KeyboardButton('🤖Покупки в Технограде❗️')
#         btn2 = types.KeyboardButton('🌃Хроники🌊')
#         markup.add(btn1, btn2)
#         bot.send_message(message.from_user.id, 'Лавка: 🤖Покупки в Технограде❗️ \nПрочитать новости: 🌃Хроники🌊 ',
#                          reply_markup=markup)  # ответ бота
#
#     elif message.text == '🤖Покупки в Технограде❗️':
#         bot.send_message(message.from_user.id,
#                          "Добро пожаловать в магазин технологий будущего Марата! "
#                          "Мы предлагаем большой выбор инновационных телефонов от ведущих мировых производителей."
#                          "У нас вы найдете самые ходовые модели, созданные с использованием последних технологических достижений."
#                          "Наша команда экспертов всегда готова проконсультировать вас по любому вопросу и помочь выбрать телефон,"
#                          "отвечающий вашим потребностям. В нашем магазине вы также можете приобрести различное дополнительное оборудование,"
#                          "такое как наушники, чехлы и другие аксессуары, для еще более комфортного использования вашего телефона."
#                          "У нас вы найдете только самые высококачественные товары по приемлемым ценам."
#                          "Приходите в наш магазин и окунитесь в мир будущего технологий!\n "
#                          '\nПолный текст можно прочитать по ' + '[ссылке](https://t.me/msk77pro)',
#                          parse_mode='Markdown')
#
#     elif message.text == '🌃Хроники🌊':
#         bot.send_message(message.from_user.id,
#                          '"Москва 2077: Хроники технограда" - это издание, посвященное жизни и событиям в технологическом мегаполисе Москва-2077. '
#                          'Ее страницы наполнены новостями о самых современных технологиях, гиперсвязи, искусственном интеллекта, кибернетике и других научных достижениях, '
#                          'которые перестали быть фантазиями ! ' + '[ссылке](https://dzen.ru/id/607fc499a17092441460fe48/)',
#                          parse_mode='Markdown')
#
#     else:
#         bot.send_message(message.from_user.id, "Попытка не удачна")
#
#
# # Запускаем бота
# if __name__ == "__main__":
#     # bot.polling()
#     bot.polling(none_stop=True, interval=0)
