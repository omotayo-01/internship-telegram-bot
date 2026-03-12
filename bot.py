import telebot



bot = telebot.TeleBot('8505756674:AAEnDZZh5_3ZtWcgtedykhTkezgrnBqeGWA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! How can i help you.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! 👋 I am an auto-reply bot.")

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.lower()

    if "hello" in text:
        bot.reply_to(message, "Hi there! 😊")

    elif "how are you" in text:
        bot.reply_to(message, "I'm fine thanks! 🤖")

    elif "help" in text:
        bot.reply_to(message, "You can say hello or ask how I am.")

    else:
        bot.reply_to(message, "Sorry, I don't understand that yet.")

print("Bot is starting... 🚀")
print("Send /start to your bot in Telegram to test")
bot.infinity_polling(timeout=20)