from aiogram import executor
import logging
from aiogram.dispatcher.filters import Text

# hw 1
from config import dp, scheduler
from handlers.basic_handlers import (info_command, help, myinfo, picture)
# hw 2
from handlers.shop import (show_categories, show_address, show_category_products)

# hw 3
from handlers.admin import (check_curses, ban_user, pin_message)
# hw 4
from handlers.user_info_fsm import (start_form, process_name, process_age,
                                    process_address, UserForm, process_delivery_day)




from db.base import (
    init_db,
    delete_table_products,
    create_tables,
    add_products,
)
# hw 6,7
from handlers.scheduler import handle_scheduler
# hw 8
from handlers.parsing_handler import parsing_handle



async def startup(_):
    init_db()
    delete_table_products()
    create_tables()
    add_products()


if __name__ == "__main__":
    # hw 1
    dp.register_message_handler(info_command, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(picture, commands=["picture"])
    # hw 2
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_category_products, Text(equals="Одежды"))
    # dp.register_callback_query_handler(show_category_clothes_callback, Text(equals='jackets'))
    # dp.register_message_handler(show_category_shoes, Text(equals="Обувь"))
    # dp.register_callback_query_handler(show_category_shoes_callback, Text(equals='slippers'))
    dp.register_message_handler(show_address, Text(equals="Адрес"))

    # hw 3
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix="/")
    dp.register_message_handler(ban_user, commands=["да"], commands_prefix=['/'])
    # hw 4
    # dp.register_message_handler(start_form, commands=["form"])
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_address, state=UserForm.address)
    dp.register_message_handler(process_delivery_day, state=UserForm.delivery_day)
    # hw 5
    dp.register_callback_query_handler(start_form, lambda callback: callback.data.startswith("buy_product_"))
    # hw 6,7
    dp.register_message_handler(handle_scheduler, Text(startswith='Напомнить'))
    # hw 8
    dp.register_message_handler(parsing_handle, commands=["cars"], commands_prefix="/")

    dp.register_message_handler(check_curses)
    scheduler.start()
    executor.start_polling(dp, on_startup=startup)

