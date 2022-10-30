import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers.echo import register_echo
from handlers.menu import register_menu
from handlers.test import register_test


def register_all_handlers(dp):
    register_menu(dp)
    register_test(dp)

    register_echo(dp)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
