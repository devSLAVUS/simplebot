import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from auth_data import token
from giro import get_all, get_weather, maska, get_pic
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
def telegram_bot(token):
    bot = Bot(token=token)
    dp = Dispatcher(bot)
    keyboard = InlineKeyboardMarkup()
    
    @dp.message_handler(commands=['m'])
    async def handle_text(message):
        await bot.send_message(message.chat.id, "<b>Введите маску: </b>", parse_mode="html")
        await bot.register_next_step_handler(message, print_mask)
    async def print_mask(message):
        txt = message.text
        s = maska(txt)
        await bot.send_message(message.chat.id, s)
    @dp.message_handler(commands=['start'])   
    async def process_start_command(message: types.Message):
        await message.reply("Команды:\n/help")
    @dp.message_handler(commands=['btc'])
    async def process_help_command(message: types.Message):
        r = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        r = requests.get(r)
        data = r.json()
        price = data["price"]
        price1 = price[:9]
        await bot.send_message(
            message.chat.id, f"{datetime.now().strftime('%d-%m-%Y      %H:%M')}\nSell BTC price: {price1}")
    @dp.message_handler(commands=['help'])
    async def help_message(message: types.Message):
        await bot.send_message(message.from_user.id, message.text)
        inf = "**Slavus Laboratories introduce**\n\
bot: lab_slavus\n\
Version: 2.1 stable\n\
Last Update: 13.10.21\n\
Команды:\n\
1./btc - курс биткоина\n\
2./pogoda - погода\n\
3./giro - гороскоп\n\
4./guys - графана"
        await bot.send_message(
            message.chat.id, inf)

    inline_btn_1 = InlineKeyboardButton('Рыбы', callback_data='fish')
    inline_btn_2 = InlineKeyboardButton('Весы', callback_data='vesi')
    inline_btn_3 = InlineKeyboardButton('Овен', callback_data='aries')
    inline_btn_4 = InlineKeyboardButton('Телец', callback_data='taurus')
    inline_btn_5 = InlineKeyboardButton('Близнецы', callback_data='gemini')
    inline_btn_6 = InlineKeyboardButton('Рак', callback_data='cancer')
    inline_btn_7 = InlineKeyboardButton('Лев', callback_data='leo')
    inline_btn_8 = InlineKeyboardButton('Дева', callback_data='virgo')
    inline_btn_9 = InlineKeyboardButton('Скорпион', callback_data='scorpio')
    inline_btn_10 = InlineKeyboardButton('Стрелец', callback_data='sagittarius')
    inline_btn_11 = InlineKeyboardButton('Козерог', callback_data='capricorn')
    inline_btn_12 = InlineKeyboardButton('Водолей', callback_data='aquarius')

    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, 
    inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12)
    
    inline_btn_13 = InlineKeyboardButton('Москва', callback_data='moscow')
    inline_btn_14 = InlineKeyboardButton('Санкт-Петербург', callback_data='spb')
    inline_btn_15 = InlineKeyboardButton('Курган', callback_data='kurgan')
    inline_btn_16 = InlineKeyboardButton('Дубаи', callback_data='dubai')
    inline_kb2 = InlineKeyboardMarkup().add(inline_btn_13, inline_btn_14, inline_btn_15, inline_btn_16)

    @dp.message_handler(commands=['giro'])
    async def process_command_1(message: types.Message):
        await message.reply("Знак?", reply_markup=inline_kb1)
    @dp.callback_query_handler(lambda c: c.data == 'vesi')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "libra"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'fish')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "pisces"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'aries')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "aries"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'taurus')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "taurus"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'gemini')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "gemini"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'cancer')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "cancer"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'leo')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "leo"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'virgo')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "virgo"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'scorpio')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "scorpio"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'sagittarius')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "sagittarius"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'capricorn')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "capricorn"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'aquarius')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "aquarius"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    
    @dp.message_handler(commands=['guys'])
    async def help_message(message: types.Message):
        await bot.send_message(message.chat.id, "<b>Загрузка графика...</b>", parse_mode="html")
        get_pic()
        time.sleep(1)
        photo = types.InputFile("/home/devslavus/reenshot.png")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    @dp.message_handler(commands=['gays'])
    async def help_message(message: types.Message):
        photo = types.InputFile("/home/devslavus/gays.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    @dp.message_handler(commands=['pogoda'])
    async def process_command_2(message: types.Message):
        await message.reply("Город?", reply_markup=inline_kb2)
    @dp.callback_query_handler(lambda c: c.data == 'moscow')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        g = "Moscow"
        s = get_weather(g)
        await bot.send_message(
                callback_query.message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                f"Хорошего дня!"
                            )
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'spb')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        g = "Saint%20Petersburg"
        s = get_weather(g)
        await bot.send_message(
                callback_query.message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                f"Хорошего дня!"
                            )
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'kurgan')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        g = "kurgan"
        s = get_weather(g)
        await bot.send_message(
                callback_query.message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                f"Хорошего дня!"
                            )
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    @dp.callback_query_handler(lambda c: c.data == 'dubai')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        g = "dubai"
        s = get_weather(g)
        await bot.send_message(
                callback_query.message.chat.id, f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                f"Погода в городе: {s[0]}\nТемпература: {s[1]}C°\n"
                                f"Влажность: {s[3]}%\nДавление: {s[4]} мм.рт.ст\nВетер: {s[5]} м/с\n"
                                f"Восход солнца: {s[6]}\nЗакат солнца: {s[7]}\nПродолжительность дня: {s[8]}\n"
                                f"Хорошего дня!"
                            )
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
       

    
    executor.start_polling(dp)

if __name__ == '__main__':
    telegram_bot(token)
