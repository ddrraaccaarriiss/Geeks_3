from aiogram import types
from random import randint
from parser.base import parse_cars


async def parsing_handle(message: types.Message):
    """
        Функция для обработки команды "/cars" и показа результата парсинга,
        функция будет отправлят каждый раз рандомно выбранные автомобили  пользователю
    """
    cars = parse_cars()
    index_ = randint(1, 10)
    await message.answer_photo(
        cars[index_]['photo'],
        caption= f"Название автомобиля:  {cars[index_]['title']}\nЦена автомобиля:  {cars[index_]['price']}\n"
    )




