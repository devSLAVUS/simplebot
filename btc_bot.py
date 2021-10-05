import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot
from auth_data import token
from telebot import types
from giro import get_all, get_weather

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        info = types.KeyboardButton('Информация')
        bitcoin = types.KeyboardButton('Курс биткоина')
        goroscope = types.KeyboardButton('Гороскоп')
        pogoda = types.KeyboardButton('Погода')
        markup.add(bitcoin, goroscope, pogoda, info)
        bot.send_message(message.chat.id, "Greetings, investor {0.first_name}!".format(message.from_user), reply_markup = markup)
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.chat.type == "private":
            if message.text == 'Курс биткоина':
                r = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
                r = requests.get(r)
                data = r.json()
                price = data["price"]
                price1 = price[:9]
                bot.send_message(
                    message.chat.id, f"{datetime.now().strftime('%d-%m-%Y      %H:%M')}\nSell BTC price: {price1}")

            elif message.text == 'Гороскоп':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                fish = types.KeyboardButton('Рыбы')
                vesi = types.KeyboardButton('Весы')
                oven = types.KeyboardButton('Овен')
                telec = types.KeyboardButton('Телец')
                bliz = types.KeyboardButton('Близнецы')
                rak = types.KeyboardButton('Рак')
                lev = types.KeyboardButton('Лев')
                deva = types.KeyboardButton('Дева')
                scorp = types.KeyboardButton('Скорпион')
                strel = types.KeyboardButton('Стрелец')
                koza = types.KeyboardButton('Козерог')
                voda = types.KeyboardButton('Водолей')
                nazad = types.KeyboardButton('Назад')
                markup.add(fish, vesi, oven, telec, bliz, rak, lev, deva, scorp, strel, koza, voda, nazad)
                bot.send_message(message.chat.id,'Гороскоп', reply_markup = markup)
            elif message.text == 'Информация':

                inf = "**Slavus Laboratories introduce**\nbot: lab_slavus\nVersion: 1.03\nLast Update: 05.10.21\nТекстовые функции:\n1. Перевод в Чизбургеры:\n   Введите команду cheese ЧИСЛО\n   В ответе получите количество чизбургеров "  
                bot.send_message(
                    message.chat.id, inf
                    )
            elif message.text == 'Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                info = types.KeyboardButton('Информация')
                bitcoin = types.KeyboardButton('Курс биткоина')
                goroscope = types.KeyboardButton('Гороскоп')
                pogoda = types.KeyboardButton('Погода')
                markup.add(bitcoin, goroscope, pogoda, info)
                bot.send_message(message.chat.id, "Welcome back! investor {0.first_name}!".format(message.from_user), reply_markup = markup)
            elif message.text == 'Весы':
                zn = "libra"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Рыбы':
                zn = "pisces"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Овен':
                zn = "aries"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Телец':
                zn = "taurus"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Близнецы':
                zn = "gemini"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Рак':
                zn = "cancer"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Лев':
                zn = "leo"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Дева':
                zn = "virgo"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Скорпион':
                zn = "scorpio"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Стрелец':
                zn = "sagittarius"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Козерог':
                zn = "capricorn"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )
            elif message.text == 'Водолей':
                zn = "aquarius"
                s = get_all(zn)         
                bot.send_message(
                    message.chat.id, f"{str(s.text)}"
                    )

            elif message.text == 'Погода':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                msk = types.KeyboardButton('Москва')
                spb = types.KeyboardButton('Санкт-Петербург')
                kur = types.KeyboardButton('Курган')
                dubai = types.KeyboardButton('Дубаи')
                nazad = types.KeyboardButton('Назад')
                markup.add(msk, spb, kur, dubai, nazad)
                bot.send_message(message.chat.id,'Погода', reply_markup = markup)

            elif message.text == 'Москва':
                g = "Moscow"
                s = get_weather(g)
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                    f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                    f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                    f"Хорошего дня!"
                                )
            
            elif message.text == 'Санкт-Петербург':
                g = "Saint%20Petersburg"
                s = get_weather(g)
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                    f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                    f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                    f"Хорошего дня!"
                                )
                
            elif message.text == 'Курган':
                g = "kurgan"
                s = get_weather(g)
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                    f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                    f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                    f"Хорошего дня!"
                                )
            elif message.text == 'Дубаи':
                g = "dubai"
                s = get_weather(g)
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                    f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                    f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                    f"Хорошего дня!"
                                )
    
            elif 'cheese' in message.text.lower():
                arg = message.text.split(maxsplit=1)[1]
                kurs = int(arg)/50
                if arg.isdigit():
                    bot.send_message(
                            message.chat.id, kurs
                            )
                else:
                    bot.send_message(
                            message.chat.id, "После команды cheese введите число!"
                            )
               
    bot.polling()
if __name__ == '__main__':
    telegram_bot(token)