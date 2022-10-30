from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='next'),
            KeyboardButton(text='exit')
        ]
    ],
    resize_keyboard=True
)

menu_java_kotlin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='java'),
            KeyboardButton(text='kotlin')
        ]
    ],
    resize_keyboard=True
)
