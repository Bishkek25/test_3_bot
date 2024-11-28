
from decouple import config
from aiogram import Dispatcher, Bot, executor, types
import logging


token = config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой телеграмм I’d: {message.from_user.id}')


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    info_text = (
        "Телеграмм бот нужен для работы и учебы"
    )
    await bot.send_message(chat_id=message.from_user.id, text=info_text)

if __name__ == '__main__':
     # logging.basicConfig(level=logging.INFO)
     executor.start_polling(dp, skip_updates=True)