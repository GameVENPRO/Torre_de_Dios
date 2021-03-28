import logging

from aiogram import Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from app import config

logging.basicConfig(format=u'%(levelname)s:[%(asctime)s] %(message)s',datefmt='%d/%m/%Y %H:%M:%S' , level=logging.INFO, 
                    handlers=[logging.FileHandler(filename="log.log", encoding='utf8'), logging.StreamHandler()])
                    
logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("gino.engine").setLevel(logging.ERROR)


storage = MemoryStorage()
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


async def startup(_):
    from app.utils.scheduler import scheduler
    scheduler.start()

    from app.database.db import connect
    await connect()
    logging.info("Base de datos estaba conectada.")

    from app.middlewares import RegisterMiddleware, DevelopmentMiddleware
    dp.middleware.setup(DevelopmentMiddleware())
    dp.middleware.setup(RegisterMiddleware())
    logging.info("Todos los middlewares se congiguraron.")

    from app import handlers
    handlers.setup(dp)
    logging.info("Todos los handlers se configuradon.")


async def shutdown(_):
    logging.info("Base de datos desconectada.")
    from app.database.db import disconnect
    await disconnect()

    from app.utils.scheduler import scheduler
    scheduler.shutdown(wait=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, 
                               on_startup=startup, 
                               on_shutdown=shutdown)
