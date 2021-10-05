import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot
from auth_data import token
from telebot import types


def telegram_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        bitcoin = types.KeyboardButton('Курс биткоина')
        goroscope = types.KeyboardButton('Гороскоп')
        pogoda = types.KeyboardButton('Погода')
        markup.add(bitcoin, goroscope, pogoda)
        bot.send_message(message.chat.id, "Greetings, investor {0.first_name}!".format(message.from_user), reply_markup = markup)
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        def get_all(znak):
            vesi = f"https://horo.mail.ru/prediction/{znak}/today/"
            request_vesi = requests.get(vesi)
            soup = BeautifulSoup(request_vesi.text, "lxml")
            giro = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
            return giro

        def get_weather(gorod):
            r = f"http://api.openweathermap.org/data/2.5/weather?q={gorod}&appid=12a7eeeda8c4becc9503870405c37f9e&units=metric"
            r = requests.get(r)
            data = r.json() 
            city = data["name"]
            cur_weather = data["main"]["temp"]
            weather_description = data["weather"][0]["main"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            wd = "Посмотри в окно, не пойму что там за погода!"
            sunrise_timestamp = datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(data["sys"]["sunrise"])
            open_weather = [city, cur_weather, weather_description, humidity, pressure, wind, sunrise_timestamp, sunset_timestamp, length_of_the_day]
            return open_weather
  
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
            elif message.text == 'Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                bitcoin = types.KeyboardButton('Курс биткоина')
                goroscope = types.KeyboardButton('Гороскоп')
                pogoda = types.KeyboardButton('Погода')
                markup.add(bitcoin, goroscope, pogoda)
                bot.send_message(message.chat.id, "Greetings, investor {0.first_name}!".format(message.from_user), reply_markup = markup)
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
               
    bot.polling()
if __name__ == '__main__':
    #get_data()   
    telegram_bot(token)
