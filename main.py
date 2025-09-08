# main.py
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from services.config import TELEGRAM_BOT_TOKEN
from services.atendimento import atendimento_router, private_router

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    # Registre os dois routers
    dp.include_router(atendimento_router)  # Para o grupo
    dp.include_router(private_router)      # Para o chat privado
    # Remove updates pendentes e inicia o bot
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
