from aiogram import types
from config import scheduler, bot





async def handle_scheduler(message: types.Message):
    """
        Функция для добавления напоминалки
    """
    global napomni
    global chat_id
    napomni = message.text[10:]
    chat_id = message.from_user.id
    scheduler.add_job(jop_handler, 'interval', seconds=10, args=(chat_id,))
    await message.answer(text='okay')



async def jop_handler(chat_id):
    """
        функция срезает слово "Напомнить" и отправляет его
    """
    print('ok')
    await bot.send_message(
        chat_id=chat_id,
        text=napomni
    )

