from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.defailt import menu


async def get_menu(message: Message):
    await message.answer(text=f'Menu : {message.text}', reply_markup=ReplyKeyboardRemove())


async def show_menu(message: Message):
    await message.answer(text='Menu', reply_markup=menu)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(get_menu,
                                lambda msg: msg.text == 'menu_1' or msg.text == 'menu_2' or msg.text == 'menu_3',
                                state='*')
    dp.register_message_handler(show_menu, commands=['menu'], state='*')
