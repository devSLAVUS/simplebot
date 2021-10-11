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
def maska(nums):
    zs = ["255.255.255.255", "1"]
    zl = ["255.255.255.254", 2]
    zo = ["255.255.255.252", 4]
    sq = ["255.255.255.248", 8]
    sg = ["255.255.255.240", 16]
    sj = ["255.255.255.224", 32]
    sb = ["255.255.255.192", 64]
    sv = ["255.255.255.128", 128]
    sa = ["255.255.255.0", 256]
    sp = ["255.255.254.0", 512]
    sh = ["255.255.252.0", 1024]
    fg = ["255.255.248.0", 2048]
    dfg = ["255.255.240.0", 4096]
    dsfsf = ["255.255.224.0", 8192]
    fghf = ["255.255.192.0", 16384]
    ytu = ["255.255.128.0", 32768]
    xcvf = ["255.255.0.0", 65536]
    sdr = ["255.254.0.0", 131072]
    serf = ["255.252.0.0", 262144]
    hgk = ["255.248.0.0", 524288]
    ghj = ["255.240.0.0", 1048576]
    tyh = ["255.224.0.0", 2097152]
    jk = ["255.192.0.0", 4194304]
    er = ["255.128.0.0", 8388608]
    hnhg = ["255.0.0.0", 16777216]
    gfh = ["254.0.0.0", 33554432]
    rdtt = ["252.0.0.0", 67108864]
    fghewrr = ["248.0.0.0", 134217728]
    rrzs = ["240.0.0.0", 268435456]
    zggs = ["224.0.0.0", 536870912]
    zvvs = ["192.0.0.0", 1073741824]
    zdfs = ["128.0.0.0", 2147483648]
    zsds = ["0.0.0.0", 4294967296]

    pool = {"32": zs, "31": zl,"30": zo, "29": sq, "28": sg, "27": sj, 
            "26": sb, "25": sv, "24": sa, "23": sp, "22": sh, "21": fg, "20": dfg}

    vivod = pool.get(nums, "Не найден")
    print (vivod)
    return "Маска: {}\nКоличество адресов: {}".format(vivod[0], vivod[1])
