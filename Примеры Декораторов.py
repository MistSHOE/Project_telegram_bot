# Обрабатывает все текстовые сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Запускаю !!!!! ")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Обрабатывает все отправленные документы и аудиофайлы
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, "Это обработчик сообщений")


# Обрабатывает все текстовые сообщения, соответствующие регулярному выражению
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
    pass


# Обрабатывает все сообщения, для которых лямбда-выражение возвращает значение True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
    pass


# Который также может быть определен как:
def test_message(message):
    return message.document.mime_type == 'text/plain'


@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
    pass


# Обработчики могут быть объединены для создания функции, которая будет вызвана, если любой из message_handler подходит
# Этот обработчик будет вызван, если сообщение начинается с '/hello' или является каким-либо эмодзи
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    pass

# использовал для ИИ
@bot.message_handler(func=lambda message: True)




bot.infinity_polling()