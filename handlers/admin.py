
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()



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
        обработчик, чтоб банить пользователя в чате
        через команду
    """
    admin_author = await is_admin(message)
    if message.chat.type != 'private':

        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
            await message.answer(f"забанили юзера {message.reply_to_message.from_user.username}")



async def check_curses(message: types.Message):
    """
        Функция отлавливает матерные слова
    """
    bad_words = ["дурак", "собака","идиот","сука"]
    if message.chat.type != 'private':
        for word in bad_words:
            if word in message.text.lower().replace(' ', ''):
                print(message.text.lower().replace(' ', ''))
                await message.reply("кикнуть пользователя за испльзование плохих слов или нет?")
                break



async def pin_message(message: types.Message):
    """
         Функция закрепляющая сообщении
    """
    if message.chat.type != 'private':
        print(message.text)
        if message.reply_to_message:
            await message.reply_to_message.pin()







