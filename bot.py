import logging
from aiogram import Bot, Dispatcher, executor, types
from config_reader import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply("Привет от pingvi! Бот пока в разработке")

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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)