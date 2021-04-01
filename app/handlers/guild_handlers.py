import logging
from contextlib import suppress
from datetime import datetime, timezone

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageToDeleteNotFound

from ..database.base import User
from ..helpers.dev_text import  user_text, heroe_text
from ..helpers.keyboards import (IDLE_Kb)
from ..utils.scheduler import scheduler
from ..utils.states import MainStates


async def user_gremio(m: Message):
    await m.answer(text'Clan', reply_markup=IDLE_Kb())
    

    


