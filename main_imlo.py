import logging
from Checkwords import Checkword

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5154638483:AAHys16ENhbFB9eJwL7NBR2galY_GiGmQXU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom, Imlo botga hush kelibsiz \n Marhamat so'zingizni yozing.")


@dp.message_handler(commands=['help'])
async def hel_menu(message: types.Message):
    await message.reply("Bot so'zingizda imloviy xato bormi yoqmi tekshirib beradi.")


@dp.message_handler()
async def checkimlo(message: types.Message):
    words = message.text
    result = Checkword(words)
    if result['available']:
        response = f"✅{words.capitalize()}"
    else:
        response = f"❌{words.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
