from aiogram import Dispatcher
from aiogram.types import Message


async def echo(message: Message):
    text = f"{message.from_user.username} : {message.text}"
    await message.reply(text=text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo, state='*')
