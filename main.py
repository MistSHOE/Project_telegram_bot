import telebot
import openai
import os

# устанавливаем ключ API OpenAI из переменной окружения
openai.api_key = ("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")

# создаем экземпляр телеграм бота
bot = telebot.TeleBot('6162983210:AAHNpEDY7LaxM_UgxFUfn6gUyJLAiI3KPjc')


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


# запускаем телеграм бота
bot.polling()




# ------------------------ СТАРЫЙ КОД ----------------------------- #

# import telebot
# import openai
#
# bot = telebot.TeleBot("6162983210:AAHNpEDY7LaxM_UgxFUfn6gUyJLAiI3KPjc")
# openai.api_key = "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"
#
#
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"{message.text}",
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     bot.send_message(message.chat.id, response.choices[0].text)
#
#
# def get_text_massages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#
#
# if __name__ == "__main__":
#     bot.polling()
