import asyncio
import logging
from aiogram import Dispatcher, Bot
from config_data.config import load_config, Config
from handlers import user_handlers
from handlers.user_handlers import Router
from keyboards.set_menu_keyboard import set_main_menu

logger = logging.getLogger(__name__)


# Делаем функцию конфигурирования и запуска бота

async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                                '[%(asctime)s] - %(name)s - %(message)s')

# Выводим в консоль
    logger.info('Starting BOT')
    config: Config = load_config()


    bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(user_handlers.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_main_menu(bot)



asyncio.run(main())











