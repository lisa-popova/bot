import logging
from aiogram import Bot, Dispatcher, executor, types
from config_reader import config
from random import randint

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="1 крутка"),
            types.KeyboardButton(text="10 круток")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Привет, Первопроходец! Хочешь сделать крутку?", reply_markup=keyboard)


@dp.message_handler(text="1 крутка")
async def one_wish(message: types.Message):
    answer = ''
    num = randint(0, 1000)
    if 1 <= num <= 700:
        answer =  'Оружие 3 звезды'
    elif 701 <= num <= 900:
        answer = 'Оружие 4 звезды'
    elif 901 <= num <= 1000:
        answer = 'Оружие 5 звёзд'
    await message.reply(answer)


#Оружие 3 звезды
#Оружие 5 звезд
#Оружие 3 звезды
#Оружие 3 звезды

@dp.message_handler(text="10 круток")
async def ten_wish(message: types.Message):
    answer = ''
    for i in range(10):
        num = randint(0, 1000)
        if 1 <= num <= 700:
            answer +=  'Оружие 3 звезды' + "\n"
        elif 701 <= num <= 900:
            answer += 'Оружие 4 звезды' + "\n"
        elif 901 <= num <= 1000:
            answer += 'Оружие 5 звёзд' + "\n"

    await message.reply(answer)

@dp.message_handler(commands="info")
async def start(message: types.Message):
    await message.reply('этот бот для круток')

@dp.message_handler(commands="photo")
async def picture(message: types.Message):
    photo = open('photo/genshin.jpg', 'rb')
    await message.answer_photo(photo=photo, caption='<3')

@dp.message_handler(commands="Arlekkino")
async def picture(message: types.Message):
    photo = open('photo/eolekino.jpg', 'rb')
    await message.answer_photo(photo=photo, caption='<3')


@dp.message_handler(commands="choose_favorite")
async def choose_favorite(message: types.Message):
    await message.reply('этот бот для круток')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
