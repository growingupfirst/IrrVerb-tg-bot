import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.text import Text
from handlers import cmd_start, on_game, on_results
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

API_TOKEN = 'token'

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=storage)
    dp.include_router(cmd_start.router)
    dp.include_router(on_game.router)
    dp.include_router(on_results.router)
    
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())