import wikipedia
import re
import telebot

bot = telebot.TeleBot("6162983210:AAHNpEDY7LaxM_UgxFUfn6gUyJLAiI3KPjc")
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")


# Функция, обрабатывающая команду /wiki
@bot.message_handler(commands=["wiki"])
def wiki(message):
    send = bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
    bot.register_next_step_handler(send, get_message_wiki)


def get_message_wiki(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


# Запускаем бота
if __name__ == "__main__":

    bot.polling(none_stop=True, interval=0)
