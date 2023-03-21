
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter



class IsAdminFilter(BoundFilter):
    """"
           Код чтобы не забанить админа
    """
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()



async def check_curses(message: types.Message):
    """
        Функция отлавливает матерные слова
    """
    bad_words = ["дурак", "собака","сука","идиот","далбаеп","блять"]
    if message.chat.type != 'private':
        for word in bad_words:
            if word in message.text.lower().replace(' ', ''):
                print(message.text.lower().replace(' ', ''))
                # await message.reply("Не ругайся")
                await message.reply(f"Админы, кикнуть пользователя {message.from_user.username} за испльзование плохих слов /да или нет?[{message.from_user.id}]")
                break



async def is_admin(message: types.Message) -> bool:
    """
        Функция вычесление админа
    """
    author_id = message.from_user.id
    admins = await message.chat.get_administrators()
    print(admins)
    for adm in admins:
        if author_id == adm['user']['id']:
            return True

    return False



async def ban_user(message: types.Message):
    """
          Oбработчик, чтоб банить пользователя в чате
          через команду
    """
    author_admin = await is_admin(message)
    if message.chat.type != 'private':
        if message.reply_to_message and author_admin:
            user_id = int(message.reply_to_message.text.split('[')[-1].replace(']', ''))
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=user_id
            )
            print(user_id)
            await message.answer(f"Забанил юзера {user_id}")



async def pin_message(message: types.Message):
    """
         Функция закрепляющая сообщения
    """
    if message.chat.type != 'private':
        print(message.text)
        if message.reply_to_message:
            await message.reply_to_message.pin()



























