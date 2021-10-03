import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot
from auth_data import token
from telebot import types
def get_data():
    r = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    r = requests.get(r)
    data = r.json()
    price = data["price"]
    print(f"{datetime.now().strftime('%d-%m-%Y     %H:%M')}\nSell BTC price:{price}")

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
                vesi = "https://horo.mail.ru/prediction/libra/today/"
                request_vesi = requests.get(vesi)

                soup = BeautifulSoup(request_vesi.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Рыбы':
                fish = "https://horo.mail.ru/prediction/pisces/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Овен':
                oven = "https://horo.mail.ru/prediction/aries/today/"
                request_oven = requests.get(oven)

                soup = BeautifulSoup(request_oven.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Телец':
                telec = "https://horo.mail.ru/prediction/taurus/today/"
                request_telec = requests.get(telec)

                soup = BeautifulSoup(request_telec.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Близнецы':
                fish = "https://horo.mail.ru/prediction/gemini/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Рак':
                fish = "https://horo.mail.ru/prediction/cancer/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Лев':
                fish = "https://horo.mail.ru/prediction/leo/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Дева':
                fish = "https://horo.mail.ru/prediction/virgo/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Скорпион':
                fish = "https://horo.mail.ru/prediction/scorpio/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Стрелец':
                fish = "https://horo.mail.ru/prediction/sagittarius/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Козерог':
                fish = "https://horo.mail.ru/prediction/capricorn/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Водолей':
                fish = "https://horo.mail.ru/prediction/aquarius/today/"
                request_fish = requests.get(fish)

                soup = BeautifulSoup(request_fish.text, "lxml")
                page_p = soup.find("div", class_ = "article__item article__item_alignment_left article__item_html")
                bot.send_message(
                    message.chat.id, f"{str(page_p.text)}"
                    )
            elif message.text == 'Москва':
                r = "http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=12a7eeeda8c4becc9503870405c37f9e&units=metric"
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
                length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(
                data["sys"]["sunrise"])
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: Москва\nТемпература: {cur_weather}C°\n"
                                    f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                                    f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                                    f"Хорошего дня!"
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
            elif message.text == 'Санкт-Петербург':
                r = "http://api.openweathermap.org/data/2.5/weather?id=498817&appid=12a7eeeda8c4becc9503870405c37f9e&units=metric"
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
                length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(
                data["sys"]["sunrise"])
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: Санкт-Петербург\nТемпература: {cur_weather}C°\n"
                                    f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                                    f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                                    f"Хорошего дня!"
                                )
            elif message.text == 'Курган':
                r = "http://api.openweathermap.org/data/2.5/weather?q=kurgan&appid=12a7eeeda8c4becc9503870405c37f9e&units=metric"
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
                length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(
                data["sys"]["sunrise"])
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: Курган\nТемпература: {cur_weather}C°\n"
                                    f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                                    f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                                    f"Хорошего дня!"
                                )
            elif message.text == 'Дубаи':
                r = "http://api.openweathermap.org/data/2.5/weather?q=dubai&appid=12a7eeeda8c4becc9503870405c37f9e&units=metric"
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
                length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(
                data["sys"]["sunrise"])
                bot.send_message(
                    message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                    f"Погода в городе: Дубаи\nТемпература: {cur_weather}C°\n"
                                    f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                                    f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                                    f"Хорошего дня!"
                                )
    bot.polling()
if __name__ == '__main__':
    #get_data()   
    telegram_bot(token)
