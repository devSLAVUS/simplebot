import requests
from bs4 import BeautifulSoup
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from auth_data import token
from giro import get_all, get_weather, maska
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

def telegram_bot(token):
    bot = Bot(token=token)
    dp = Dispatcher(bot)
    keyboard = InlineKeyboardMarkup()
    menu_1 = InlineKeyboardButton(text='Расписание 🗓', callback_data="menu_1")
    menu_2 = InlineKeyboardButton(text='Программы 💾', callback_data="menu_2")
    menu_3 = InlineKeyboardButton(text='О проекте  📌', callback_data="menu_3")
    keyboard.add(menu_1, menu_2, menu_3)

    @dp.message_handler(commands=['start'])
    async def process_start_command(message: types.Message):
        await message.reply("Привет!\nНапиши мне что-нибудь!")
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
Version: 2.0 stable\n\
Last Update: 12.10.21\n\
Команды:\n\
1./btc - курс биткоина\n\
2./pogoda - погода\n\
3./giro - гороскоп\n\
"
        await bot.send_message(
            message.chat.id, inf)

    inline_btn_1 = InlineKeyboardButton('Весы', callback_data='vesi')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

    @dp.message_handler(commands=['1'])
    async def process_command_1(message: types.Message):
        await message.reply("Знак?", reply_markup=inline_kb1)
    @dp.callback_query_handler(lambda c: c.data == 'vesi')
    async def process_callback_button1(callback_query: types.CallbackQuery):
        zn = "libra"
        s = get_all(zn)         
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.message.chat.id, f"{str(s.text)}")
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id) 

    
    executor.start_polling(dp)

if __name__ == '__main__':
    telegram_bot(token)
