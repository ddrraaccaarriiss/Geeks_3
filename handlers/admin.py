from aiogram import types


# async def example(message: types.Message):
#     """
#         Функция вычесление админа
#     """
#     # print(message.chat.type)
#     if message.chat.type != 'private':
#         print(message.text)
#         admins = await message.chat.get_administrators()
#         for a in admins:
#             print(a["user"]["username"])
#         await message.answer("Привет")


# async def check_curses(message: types.Message):
#     """
#         Функция отлавливает матерные слова
#     """
#     bad_words = ["дурак", "собака"]
#     if message.chat.type != 'private':
#         for word in bad_words:
#             if word in message.text.lower().replace(' ', ''):
#                 print(message.text.lower().replace(' ', ''))
#                 await message.reply("Не ругайся")
#                 break










