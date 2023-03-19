# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
#
#
# # FSM - Finite State Mashine
# class UserForm(StatesGroup):
#     name = State()
#     age = State()
#     address = State()
#
#
# async def start_form(message: types.Message):
#     await UserForm.name.set()
#     await message.answer("Как вас зовут?")
#
#
# async def process_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await UserForm.next()
#     await message.answer("Сколько вам лет?")
#
#
# async def process_age(message: types.Message, state: FSMContext):
#     # if not message.text.isdigit():
#     #     await message.answer("ВВедите только цифры")
#     # else:
#     async with state.proxy() as data:
#         data['age'] = message.text
#     await UserForm.next()
#     await message.answer("Какой у вас адрес?")
#
#
# async def process_address(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['address'] = message.text
#         print(data)
#
#     await state.finish()
#     await message.answer("Спасибо.")