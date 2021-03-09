from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

import logging


class DevelopmentMiddleware(BaseMiddleware):
    async def development(self, m: types.Message, is_admin):
        from ..config import DEVELOPMENT_MODE
        if DEVELOPMENT_MODE and not is_admin:
            print(f"[DEV_MODE] \"{m.text}\"  -  {m.from_user.id} | {m.from_user.first_name}")
            await m.answer('El bot está en un estado de desarrollo. \nTiempo de espera Aproximado: <i>5-∞</i>min. \nInformación adicional- @JuanShotLC')
            raise CancelHandler()

    async def on_pre_process_message(self, m: types.Message, *args, **kwargs):
        await self.development(m, True if m.from_user.id == 622952731 else False)

    async def on_pre_process_callback_query(self, c: types.CallbackQuery, *args, **kwargs):
        await self.development(c.message, True if c.from_user.id == 622952731 else False)

