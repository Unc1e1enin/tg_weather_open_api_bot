import telebot
import requests
from datetime import datetime

tg_token = 'tg_token'
weather_api_token = 'weather_api_token'

bot = telebot.TeleBot(tg_token)


@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, 'Напиши название города и я пришлю тебе сводку погоды ')

@bot.message_handler(func=lambda message: True)
def get_weather(message):
  try:
    weather_data_req = requests.get( f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_api_token}&units=metric")
    weather_data = weather_data_req.json()
    city = weather_data['name']
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    wind = weather_data['wind']['speed']

    bot.reply_to(message, f'Погода в городе {city}:\nТемпература {temp}C°\nВлажность: {humidity}%\nДавление: {pressure} мм. рт.ст.\nВетер: {wind}  м\с')

  except:
    bot.reply_to(message, 'Проверьте название города')

    
bot.infinity_polling()
    
