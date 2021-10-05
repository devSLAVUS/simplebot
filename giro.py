from bs4 import BeautifulSoup
import requests
from datetime import datetime
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