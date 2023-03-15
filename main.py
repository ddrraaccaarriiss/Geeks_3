from aiogram import executor
import logging
from aiogram.dispatcher.filters import Text

# from handlers.admin import check_curses
# from handlers.admin import example
from config import dp
from handlers.basic_handlers import (start,help,myinfo,picture,all_sms)
from handlers.shop import (show_categories,show_category_clothes,
                           show_category_clothes_callback,
                           show_category_shoes,
                           show_category_shoes_callback,
                           show_address)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(show_categories,commands=["start"])
    dp.register_message_handler(show_category_clothes, Text(equals="Одежды"))
    dp.register_callback_query_handler(show_category_clothes_callback, Text(equals='jackets'))
    dp.register_message_handler(show_category_shoes, Text(equals="Обувь"))
    dp.register_callback_query_handler(show_category_shoes_callback, Text(equals='slippers'))
    dp.register_message_handler(show_address, Text(equals="Адрес"))

    dp.register_message_handler(start,commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(picture, commands=["picture"])

    # dp.register_message_handler(example)
    # dp.register_message_handler(check_curses)
    dp.register_message_handler(all_sms)
    executor.start_polling(dp)
