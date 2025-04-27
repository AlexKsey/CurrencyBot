import telebot
from extensions import Converter, APIException
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

currencies = {'доллар': 'USD', 'евро': 'EUR', 'рубль': 'RUB'}

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, что бы возпользоваться конвертором Отправь: валюта1 валюта2 количество\nПример: доллар рубль 100 ")

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "Отправьте: валюта1 валюта2 количество\nПример: доллар рубль 100")

@bot.message_handler(commands=['values'])
def values(message):
    bot.send_message(message.chat.id, "\n".join([f"{k} ({v})" for k, v in currencies.items()]))

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        base, quote, amount = message.text.split()
        result = Converter.get_price(currencies[base.lower()], currencies[quote.lower()], float(amount))
        bot.send_message(message.chat.id, f"Результат: {result}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")



bot.polling()