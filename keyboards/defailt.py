from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='menu_1')
        ],
        [
            KeyboardButton(text='menu_2'),
            KeyboardButton(text='menu_3')
        ]
    ],
    resize_keyboard=True
)

