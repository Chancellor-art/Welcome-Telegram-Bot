import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(content_types=['new_chat_members'])

def welcome(message):
    bot.reply_to(message, text='Добро пожаловать в нашу дружную семью)')

bot.polling(none_stop=True)