from aiogram import executor
import logging
from aiogram.dispatcher.filters import Text

from config import dp
from handlers.basic_handlers import (help,myinfo,picture)
from handlers.shop import (show_categories,show_category_clothes,
                           show_category_clothes_callback,
                           show_category_shoes,
                           show_category_shoes_callback,show_address)


from handlers.admin import (check_curses,ban_user,pin_message)






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(show_categories,commands=["start"])
    dp.register_message_handler(show_category_clothes, Text(equals="Одежды"))
    dp.register_callback_query_handler(show_category_clothes_callback, Text(equals='jackets'))
    dp.register_message_handler(show_category_shoes, Text(equals="Обувь"))
    dp.register_callback_query_handler(show_category_shoes_callback, Text(equals='slippers'))
    dp.register_message_handler(show_address, Text(equals="Адрес"))

    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(picture, commands=["picture"])

    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix="/")
    dp.register_message_handler(ban_user, commands=["да"],commands_prefix=['/'])
    dp.register_message_handler(check_curses)

    executor.start_polling(dp)

