import logging

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.dispatcher.filters.builtin import Command, IDFilter

from ..utils.states import MainStates, AdminStates
from .base_handlers import *
from .user_handlers import *
from .batle_handlers import *
from .guild_handlers import *


AVAILABLE_COMMANDS = ("⚔️Atacar", "🗺Misiones", "🛡Defender","🏅Yo","🏰Castillo", "👥Clanes" ,'/help', '/heroe','/stock','/inv','/crearclan')
ADMIN_COMMANDS = ('lambda', 'info', 'log', 'get', 'deluser', 'broadcast', 'sbroadcast', 'reload')


def setup(dp: Dispatcher):
    # BASE HANDLERS:
     
    dp.register_message_handler(cmd_start, CommandStart())
    dp.register_message_handler(user_registro, lambda m: m.text and m.data in ['🐉Escama de dragon','🌑Luz lunar','🥔Papa','🦅Nido alto','🐺Manada de lobos','🦌Cuerno de ciervo','🦈Dientes de Tiburón'])
    
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
    dp.register_message_handler(user_profile, lambda m: m.text and m.text == '🛡Defender')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '⚔️Atacar')
    dp.register_message_handler(user_atacar, lambda m: m.text and m.data in ['🐉','🌑','🥔','🦅','🐺','🦌','🦈'])
    dp.register_callback_query_handler(mision_pve, lambda c: True and c.data in ['bosque','pantano','valle','foray','arena'], state='*')

    
    # GAME HANDLERS:

    # GEAR HANDLERS:
       

    # USER HANDLERS:

    dp.register_message_handler(user_profile, lambda m: m.text and m.text == '🏅Yo')
    dp.register_message_handler(user_misiones, lambda m: m.text and m.text == '🗺Misiones')
    dp.register_message_handler(user_castillo, lambda m: m.text and m.text == '🏰Castillo')
    dp.register_message_handler(user_clan, lambda m: m.text and m.text == '👥Clanes')
    dp.register_message_handler(user_anu, lambda m: m.text and m.text == '💬')
    
    
    
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/heroe')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/inv')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/alm')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/efectos')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/top')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/worldtop')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/promo')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/reporte')
    dp.register_message_handler(user_heroe, lambda m: m.text and m.text == '/level_up')
    dp.register_message_handler(user_gremio, lambda m: m.text and m.text == '/creargremio')
    # ...


