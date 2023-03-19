
from aiogram import types
import os
import random



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




async def myinfo(message: types.Message):
    """
        Функция показывает информацию о пользователе
    """
    id = message.from_user.id
    first_name = message.from_user.first_name
    user_name = message.from_user.username
    await message.reply(f"Ваш id: {id}\nВаш first_name: {first_name}\nВаш user_name: {user_name}")



async def picture(message: types.Message):
    """
        Функция отправляет картинку
    """
    # Получаем список файлов в папке images
    files = os.listdir('images')
    # Выбираем случайное имя файла
    filename = random.choice(files)
    # Отправляем файл пользователю
    with open(f"images/{filename}", "rb") as file:
        await message.answer_photo(file)
        await message.delete()


