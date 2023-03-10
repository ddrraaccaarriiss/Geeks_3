from aiogram import Bot, Dispatcher, executor, types
import logging
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def info_command(message: types.Message):
    """
        Функция приветствия пользователя по имени
    """
    await message.answer(f"Приветствую тебя, {message.from_user.first_name}")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """
        Функция показывает команды
    """
    menu = (
        "/start - начать диалог\n"
        "/help - показать меню\n"
        "/myinfo - получить информацию\n"
        "/picture - получить случайную картинку\n"
    )
    await message.reply(f"Список команд:\n{menu}")


@dp.message_handler(commands=['myinfo'])
async def myinfo(message: types.Message):
    """
        Функция показывает информацию о пользователе
    """
    id = message.from_user.id
    first_name = message.from_user.first_name
    user_name = message.from_user.username
    await message.reply(f"Ваш id: {id}\nВаш first_name: {first_name}\nВаш user_name: {user_name}")


@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    """
        Функция отправляет картинку
    """
    with open('images/ps.jpg', 'rb') as img:
        await message.answer_photo(photo=img)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)

# pip freeze > requirements.txt