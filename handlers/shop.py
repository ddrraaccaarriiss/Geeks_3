from aiogram import types

kb = types.ReplyKeyboardMarkup()
kb.add(types.KeyboardButton("Одежды"),types.KeyboardButton("Обувь"),types.KeyboardButton("Адрес"))
# kb.add(types.KeyboardButton("Обувь"))
# kb.add(types.KeyboardButton("Наш адрес))



async def show_categories(message: types.Message):
    """
        Функция показывает категории товаров
    """
    await message.reply("Наш магазин одежды", reply_markup=kb)




async def show_category_clothes(message: types.Message):
    """
        Функция показывает категорию одежды
    """
    kb_с = types.InlineKeyboardMarkup()
    kb_с.add(types.InlineKeyboardButton(text="Куртки", callback_data='jackets'),
             types.InlineKeyboardButton(text="Брюки",url='https://alex.kg/product-category/turisticheskoe-snaryazhenie/odezhda-dlya-turizma/bryuki-dlya-turizma-i-trekinga/')
             )
    await message.answer("Наши одежды",reply_markup=kb_с)


async def show_category_clothes_callback(callback: types.CallbackQuery):
    """
        Функция показывает колбек одежды
    """
    await callback.message.answer("их нет в наличии")




async def show_category_shoes(message: types.Message):
    """
        Функция показывает категорию обуви
    """
    kb_shoes = types.InlineKeyboardMarkup()
    kb_shoes.add(types.InlineKeyboardButton(text="Бутсы",url='https://lion.kg/ru'),
                 types.InlineKeyboardButton(text="тапочки",callback_data='slippers'))
    # kb_shoes.add(types.InlineKeyboardButton(text="Бутсы",url='https://lion.kg/ru'))
    # kb_shoes.add(types.InlineKeyboardButton(text="тапочки", callback_data='slippers'))
    await message.answer("Наши обуви",reply_markup=kb_shoes)


async def show_category_shoes_callback(callback: types.CallbackQuery):
    """
        Функция показывает колбек обуви
    """
    await callback.answer("их нет в наличии")




async def show_address(message: types.Message):
    """
        Функция показывает адрес магазина
    """
    await message.answer("г.Бишкек, ул.Чуйская 12.")


