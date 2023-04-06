from aiogram import types
from config import scheduler, bot




async def handle_scheduler(message: types.Message):
    """
        Функция для добавления напоминалки
    """
    text = message.text[10:]
    chat_id = message.from_user.id
    scheduler.add_job(jop_handler, 'cron', second=1, args=(text, chat_id,))
    await message.answer(text='okay')



async def jop_handler(text, chat_id,):
    """
        функция срезает слово "Напомнить" и отправляет его
    """
    print('ok')
    await bot.send_message(
        chat_id=chat_id,
        text=text
    )

