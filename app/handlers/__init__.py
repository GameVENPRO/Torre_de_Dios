import logging

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.dispatcher.filters.builtin import Command, IDFilter

from ..utils.states import MainStates, AdminStates
from .base_handlers import *
from .user_handlers import *


AVAILABLE_COMMANDS = ("⚔️Atacar", "🗺Misiones", "🛡Defender","🏅Yo","🏰Castillo", "👥Clanes" ,'/help', '/heroe','/stock','/inv')
ADMIN_COMMANDS = ('lambda', 'info', 'log', 'get', 'deluser', 'broadcast', 'sbroadcast', 'reload')


def setup(dp: Dispatcher):
    # BASE HANDLERS:
     
    dp.register_message_handler(cmd_start, CommandStart())
    # ...
    dp.register_message_handler(help_func, CommandHelp())
    dp.register_message_handler(help_func, lambda m: m.text and m.text == '🔈 Asistencia')
    dp.register_callback_query_handler(help_query, lambda c: True and c.data[:5] == "help_")
    # ...
    dp.register_message_handler(admin_commands, IDFilter(user_id=622952731), Command(commands=ADMIN_COMMANDS, prefixes='!'), state='*')
    dp.register_message_handler(admin_get_handler, IDFilter(user_id=622952731), state=AdminStates.getuser)
    dp.register_message_handler(admin_del_handler, IDFilter(user_id=622952731), state=AdminStates.deluser)
    # ...
    dp.register_message_handler(IDLE, lambda m: m.text and not m.text.startswith(('!', '/')) and m.text not in AVAILABLE_COMMANDS)
    dp.register_callback_query_handler(back, lambda c: True and c.data == 'back', state='*')
    # ...
    dp.register_errors_handler(errors_handler)

    # BATTLE HANDLERS:
   
    # GAME HANDLERS:

    # GEAR HANDLERS:

    # USER HANDLERS:

    dp.register_message_handler(user_profile, lambda m: m.text and m.text == '🏅Yo')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/heroe')
    # ...


