import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
import common


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(TOKEN)
    dp.include_router(common.router)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except RuntimeError as e:
        print(e)


if __name__ == '__main__':
    asyncio.run(main())
