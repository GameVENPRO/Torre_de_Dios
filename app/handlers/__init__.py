import logging

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.dispatcher.filters.builtin import Command, IDFilter

from ..utils.states import MainStates, AdminStates
from .base_handlers import *
from .battle_handlers import *
from .game_handlers import *
from .gear_handlers import *
from .user_handlers import *


AVAILABLE_COMMANDS = ("👤 Perfil", "⚔️ Combate", "💉 Tratamiento", "🧪 Pociones curativas", "📯 Ascenso de rango",
                      "💊 Enfermería", "💼 Inventario", "📤 Retirar el equipo", "🥋 Equipamiento",
                      "⚖️ Mejorar las características", "⚒ Kraft", "🔈 Asistencia", "🎲 Capacidades",
                      "🛒 Mercado", '/help')
ADMIN_COMMANDS = ('lambda', 'info', 'log', 'get', 'deluser', 'broadcast', 'sbroadcast', 'reload')


def setup(dp: Dispatcher):
    # BASE HANDLERS:
     
    dp.register_message_handler(cmd_start, CommandStart())
    # ...
    dp.register_message_handler(help_func, CommandHelp())
    dp.register_message_handler(help_func, lambda m: m.text and m.text == '🔈 Asistencia')
    dp.register_callback_query_handler(help_query, lambda c: True and c.data[:5] == "help_")
    # ...
    dp.register_message_handler(admin_commands, IDFilter(user_id=397247994), Command(commands=ADMIN_COMMANDS, prefixes='!'), state='*')
    dp.register_message_handler(admin_get_handler, IDFilter(user_id=397247994), state=AdminStates.getuser)
    dp.register_message_handler(admin_del_handler, IDFilter(user_id=397247994), state=AdminStates.deluser)
    # ...
    dp.register_message_handler(IDLE, lambda m: m.text and not m.text.startswith(('!', '/')) and m.text not in AVAILABLE_COMMANDS)
    dp.register_callback_query_handler(back, lambda c: True and c.data == 'back', state='*')
    # ...
    dp.register_errors_handler(errors_handler)

    # BATTLE HANDLERS:

    dp.register_message_handler(pve_rankup, lambda m: m.text and m.text == '📯 Ascenso de rango')
    # ...
    dp.register_message_handler(pve_battle, lambda m: m.text and m.text == '⚔️ Combate')
    dp.register_callback_query_handler(pve_confirmed, lambda c: True and c.data == 'battle_state', state=MainStates.battle)
    dp.register_message_handler(pve_leave_battle, lambda m: m.text and m.text == '⛔️ Rendirse', state=MainStates.battle)    
    # ...
    dp.register_callback_query_handler(pve_attack_menu, lambda c: True and c.data == 'attack_menu', state=MainStates.battle)
    dp.register_callback_query_handler(pve_defence_menu, lambda c: True and c.data == 'defence_menu', state=MainStates.battle)
    dp.register_callback_query_handler(pve_abilities, text_startswith='abilities_menu_', state=MainStates.battle)
    dp.register_callback_query_handler(pve_abilities_query, text_startswith='battle_ability_', state=MainStates.battle)
    # ...
    dp.register_callback_query_handler(pve_attack, lambda c: True and c.data == 'attack_mob', state=MainStates.battle)
    dp.register_callback_query_handler(pve_defence, lambda c: True and c.data == 'defence_mob', state=MainStates.battle)
    
    # GAME HANDLERS:

    dp.register_message_handler(shop_all, lambda m: m.text and m.text == '🛒 Mercado')
    # ...
    dp.register_callback_query_handler(shop_query_my, lambda c: True and c.data == 'shop_my', state=MainStates.shopping)
    dp.register_callback_query_handler(shop_query_refresh, lambda c: True and c.data[:12] == 'shop_refresh', state=MainStates.shopping)
    # ...
    dp.register_callback_query_handler(shop_query_get, lambda c: True and c.data[:9] == 'shop_get_', state=MainStates.shopping)
    dp.register_callback_query_handler(shop_query_delete, lambda c: True and c.data[:16] == 'shop_lot_delete_', state=MainStates.shopping)
    dp.register_callback_query_handler(shop_query_buy, lambda c: True and c.data[:13] == 'shop_lot_buy_', state=MainStates.shopping)
    # ...
    dp.register_callback_query_handler(shop_query_scroll, lambda c: True and c.data[:5] == 'shop_', state=MainStates.shopping)
    # ...
    dp.register_callback_query_handler(buy_heal_potion, lambda c: True and c.data == 'buy_heal_potion')

    # GEAR HANDLERS:

    dp.register_message_handler(gear_info_check, lambda m: m.text and m.text.startswith('/'))
    # ...
    dp.register_callback_query_handler(gear_equip, lambda c: True and c.data[:6] == 'equip_')
    dp.register_message_handler(gear_unequip, lambda m: m.text and m.text == '📤 Retirar el equipoу')
    dp.register_callback_query_handler(gear_unequip_query, lambda c: True and c.data[:8] == 'unequip_' and c.data[8:] != 'empty')
    # ...
    dp.register_message_handler(gear_craft, lambda m: m.text and m.text == '⚒ Kraft')
    dp.register_callback_query_handler(gear_craft_query, lambda c: True and c.data[:6] == 'craft_')
    # ...
    dp.register_callback_query_handler(gear_sell_register, lambda c: True and c.data[:14] == 'sell_register_')
    dp.register_callback_query_handler(gear_sell_confirm, lambda c: True and c.data[:5] == 'sell_')
    dp.register_message_handler(gear_sell_registered, lambda m: m.text, state=MainStates.selling)
    
    # USER HANDLERS:

    dp.register_message_handler(user_profile, lambda m: m.text and m.text == '👤 Perfil')
    # ...
    dp.register_message_handler(user_inventory, lambda m: m.text and m.text == '💼 Inventario')
    dp.register_callback_query_handler(user_inventory_items, lambda c: True and c.data[:4] == 'inv_')
    dp.register_message_handler(user_equipment, lambda m: m.text and m.text == '🥋 Equipamiento')
    # ...
    dp.register_message_handler(user_healing_options, lambda m: m.text and m.text == '💉 Tratamiento')
    dp.register_message_handler(user_heal, lambda m: m.text and m.text == '🧪 Pociones curativas')
    dp.register_callback_query_handler(user_heal_query, lambda c: True and c.data == 'use_heal_potion')   
    # ...
    dp.register_message_handler(user_healing, lambda m: m.text and m.text == '💊 Enfermería')
    dp.register_callback_query_handler(user_healing_query, lambda c: True and c.data == 'enter_healing')
    dp.register_message_handler(user_healing_cancel, lambda m: m.text and m.text == '🔚 Salir de la enfermería', state=MainStates.healing)
    dp.register_message_handler(user_healing_info, lambda m: m.text and m.text == '❔ Información', state=MainStates.healing)
    # ...
    dp.register_message_handler(user_stats_increase, lambda m: m.text and m.text == '⚖️ Mejorar las características')
    dp.register_callback_query_handler(user_stats_increase_query, lambda c: True and c.data[:13] == 'update_level_')
    # ...
    dp.register_message_handler(user_abilities, text='🎲 Capacidades')
    dp.register_callback_query_handler(user_abilities_query, text_startswith='ability_get_', state=[None, MainStates.battle])
