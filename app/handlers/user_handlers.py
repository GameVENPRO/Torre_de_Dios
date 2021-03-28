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


async def user_profile(m: Message, user: User, clean=True):
    await m.answer(text=user_text(user, user.username), reply_markup=IDLE_Kb())
    
async def user_heroe(m: Message, user: User, clean=True):
    await m.answer(text=heroe_text(user, user.username), reply_markup=IDLE_Kb())

