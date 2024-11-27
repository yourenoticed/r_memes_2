from os import environ
from asyncio import run
from aiogram import Bot, Dispatcher
from handlers.handlers import router


async def main():
    bot = Bot(environ.get("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
