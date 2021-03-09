from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# MAIN KEYBOARDS:
def IDLE_Kb():
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    main_kb.add(
        KeyboardButton(text='👤 Perfil')).add(
        KeyboardButton(text='💼 Inventario')).add(
        KeyboardButton(text='⚔️ Combate')).add(
        KeyboardButton(text='💉 Tratamiento'))
    return main_kb


def PROFILE_Kb():
    pfl_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    pfl_kb.row(KeyboardButton(text='🥋 Equipamiento'),
               KeyboardButton(text='⚖️ Mejorar las características'))
    pfl_kb.row(KeyboardButton(text='📯 Ascenso de rango'),
               KeyboardButton(text='🔙 Atrás'))
    return pfl_kb


def EQUIPMENT_Kb():
    reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reply_kb.add(
        KeyboardButton(text='📤 Retirar el equipo')).add(
        KeyboardButton(text='⚒ Kraft')).add(
        KeyboardButton(text='🛒 Mercado')).add(
        KeyboardButton(text='🔙 Atrás'))
    return reply_kb


def HEALING_Kb():
    reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reply_kb.add(
        KeyboardButton(text='💊 Enfermería')).add(
        KeyboardButton(text='🧪 Pociones curativas')).add(
        KeyboardButton(text='🔙 Atrás'))
    return reply_kb


def STATS_INC_Kb():
    kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton(text="⚖️ Mejorar las características"), KeyboardButton(text="🔙 Atrás"))
    return kb


def SHOP_Kb(queue, page):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.row(InlineKeyboardMarkup(text='👤 A mis lotes', callback_data='shop_my'), 
           InlineKeyboardMarkup(text='🔄 Renovar', callback_data='shop_refresh'))
    if queue: 
        kb.add(*[InlineKeyboardButton(text=f'{item.item} - 💰{item.price}', callback_data=f'shop_get_{item.id}') for item in queue[page*5:page*5+5]])
    else:
        kb.add(InlineKeyboardMarkup(text='-', callback_data='empty'))
    kb.row(InlineKeyboardMarkup(text='◀️', callback_data='shop_back'), 
           InlineKeyboardMarkup(text=f'{page+1}/{len(queue)//5+1 if len(queue)%5>0 else len(queue)//5}', callback_data='empty'), 
           InlineKeyboardMarkup(text='▶️', callback_data='shop_forward'))
    kb.add(InlineKeyboardButton(text="🔚 Cerrar", callback_data='back'))
    return kb


def SHOP_MY_Kb(queue, page):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.row(InlineKeyboardMarkup(text='🌐 A todos los lotes', callback_data='shop_refresh'),
           InlineKeyboardMarkup(text='🔄 Renovar', callback_data='shop_refresh_my'))
    kb.add(*[InlineKeyboardButton(text=f'{item.item} - 💰{item.price}', callback_data=f'shop_get_my_{item.id}') for item in queue[page*5:page*5+5]])
    kb.row(InlineKeyboardMarkup(text='◀️', callback_data='shop_my_back'), 
           InlineKeyboardMarkup(text=f'{page+1}/{len(queue)//5+1 if len(queue)%5>0 else len(queue)//5}', callback_data='empty'), 
           InlineKeyboardMarkup(text='▶️', callback_data='shop_my_forward')).add(
           InlineKeyboardButton(text="🔚 Cerrar", callback_data='back')) 
    return kb


def SHOP_MY_LOT_Kb(lot):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text='🚫 Cancelar lote', callback_data=f'shop_lot_delete_{lot}')).add(
           InlineKeyboardButton(text='🔙 Atrás', callback_data='shop_refresh_my'))
    return kb


def SHOP_LOT_Kb(lot):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text='💸 Comprar un artículo', callback_data=f'shop_lot_buy_{lot}')).add(
           InlineKeyboardButton(text='🔙 Atrás', callback_data='shop_refresh'))
    return kb


def ATTACK_Kb():
    attack_keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="◾ Cabeza", callback_data="attack_mob")
    btn2 = InlineKeyboardButton(text="▫ Pecho", callback_data="attack_mob")
    btn3 = InlineKeyboardButton(text="◾ Vientre", callback_data="attack_mob")
    btn4 = InlineKeyboardButton(text="▫ Pie", callback_data="attack_mob")
    attack_keyboard.add(btn1, btn2, btn3, btn4)
    return attack_keyboard


def BATTLE_MENU_Kb(first_text, first_callback, attack: bool):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text=first_text, callback_data=first_callback)).add(
           InlineKeyboardButton(text="🎲 Capacidades", callback_data=f"abilities_menu_{'atk' if attack else 'def'}"))
    return kb


def ABILITIES_Kb(abilities, battle: bool, attack: bool = True):
    kb = InlineKeyboardMarkup(row_width=1)
    for i in range(len(abilities)):
        kb.add(InlineKeyboardButton(text=f'{abilities[i].name}:  \"{abilities[i].rank}\"', 
                                    callback_data=f"ability_get_{('atk_' if attack else 'def_') if battle else ''}{abilities[i].id}"))
    kb.add(InlineKeyboardButton(text="🔚 Cerrar", 
                                callback_data=('attack_menu' if attack else 'defence_menu') if battle else 'back'))
    return kb


def ABILITIES_ITEM_Kb(clear=True, item=0, attack: bool = True):
    kb = InlineKeyboardMarkup(row_width=1)
    if clear:
        kb.add(InlineKeyboardButton(text='🔙 Atrás', callback_data='ability_get_back'))
    else:
        mode = 'atk' if attack else 'def'
        kb.add(InlineKeyboardButton(text='🎲 Utilizar', callback_data=f'battle_ability_{mode}_use_{item}')).add(
               InlineKeyboardButton(text='🔙 Atrás', callback_data=f"battle_ability_{mode}_back"))
    return kb


def DEFENCE_Kb():
    defence_keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="▫ Cabeza", callback_data="defence_mob")
    btn2 = InlineKeyboardButton(text="◾ Pecho", callback_data="defence_mob")
    btn3 = InlineKeyboardButton(text="▫ Vientre", callback_data="defence_mob")
    btn4 = InlineKeyboardButton(text="◾ Pie", callback_data="defence_mob")
    defence_keyboard.add(btn1, btn2, btn3, btn4)
    return defence_keyboard


def CONFIRM_BATTLE_Kb():
    kb = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="⚔️ ¡A la batalla!", callback_data="battle_state")
    button2 = InlineKeyboardButton(text="✖️ Huir", callback_data="back")
    kb.add(button1, button2)
    return kb


def PVE_LEAVE_Kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('⛔️ Rendirse'))


def INVENTORY_ITEM_Kb(item_id):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text='📥 Poner el objeto', callback_data=f"equip_{item_id}"),
           InlineKeyboardButton(text='💸 Vender el artículo', callback_data=f'sell_{item_id}'),
           InlineKeyboardButton(text='🔙 Atrás', callback_data=f"equip_back"))
    return kb


def UNDRESS_Kb(data):
    kb = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text=f"{data[0]}", callback_data=f'unequip_{data[1]}')
    btn2 = InlineKeyboardButton(text=f"{data[2]}", callback_data=f'unequip_{data[3]}')
    btn3 = InlineKeyboardButton(text="🔙 Atrás", callback_data='back')
    kb.add(btn1, btn2, btn3)
    return kb


def UPDATE_STATS_Kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        *[InlineKeyboardButton(x, callback_data=f'update_level_{y}') for x, y in
          {'🗡 Daño +1': 'damage', '♥ Salud +1': 'health', '🛡 Protección +1': 'defence'}.items()]).add(
        InlineKeyboardButton(text="🔚 Cerrar", callback_data='back'))
    return kb


def HEAL_CONFIRM_Kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text="💉 Sí", callback_data="use_heal_potion"))
    kb.add(InlineKeyboardButton(text="🔚 Cerrar", callback_data="back"))
    return kb


def HEAL_PURCHASE_Kb(minus):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton(text=f"Adquirir -{minus} monedas", callback_data="buy_heal_potion"))
    kb.add(InlineKeyboardButton(text="🔚 Cerrar", callback_data="back"))
    return kb


def INVENTORY_Kb(inv):
    kb = InlineKeyboardMarkup(row_width=1)
    for i in range(len(inv)):
        kb.add(InlineKeyboardButton(text=inv[i].name, callback_data=f"inv_{inv[i].id}"))
    kb.add(InlineKeyboardButton(text="🔚 Cerrar", callback_data="back"))
    return kb


def CRAFT_Kb(inv):
    kb = InlineKeyboardMarkup(row_width=1)
    for i in range(len(inv)):
        kb.add(InlineKeyboardButton(text=f"x2 {inv[i].name}", callback_data=f"craft_{inv[i].id}"))
    kb.add(InlineKeyboardButton(text="🔙 Atrás", callback_data="back"))
    return kb


def HELP_Kb():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(*[InlineKeyboardButton(x, callback_data=f"help_menu_{y}") for x, y in
           {'Formación (es recomendable)': 'train', 'Descripción del bot del juego': 'desc', 'Bot funcional': 'func'}.items()])
    kb.row(InlineKeyboardButton(text='🔈 Demás..', callback_data='help_menu_other'),
           InlineKeyboardButton(text='🔚 Cerrar', callback_data='back'))
    return kb


def FUNC_LIST_Kb():
    kb = InlineKeyboardMarkup(row_width=2)
    commands = ("👤 Perfil", "⚔️ Combate",
                "💉 Curación", "📯 Ascenso de rango", "💼 Inventario", "📤 Retirar el equipo", "🥋 Equipamiento",
                "⚖️ Mejorar las características", "⚒ Kraft", "🔈 Asistencia", "🛒 Tienda")
    kb.add(*[InlineKeyboardButton(name, callback_data=f"help_{name}") for name in commands]).insert(
        InlineKeyboardButton(text="🔙 Atrás", callback_data="help_back"))
    return kb


# def ADMIN_GET_Kb(matches):
#     kb = InlineKeyboardMarkup(row_width=1)
#     for i in range(len(matches)):
#         kb.insert(
#             InlineKeyboardButton(text=matches[i].username, callback_data=f"get_{matches[i].telegram_id}"))
#     return kb


def CONFIRM_Kb(text: tuple, callback: str, row_width: int = 2):
    kb = InlineKeyboardMarkup(row_width=row_width)
    kb.row(InlineKeyboardButton(text=text[0], callback_data=callback), 
           InlineKeyboardButton(text=text[1], callback_data='back'))
    return kb


def HEALING_STATE_Kb():
    reply_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    reply_kb.add(*[
        KeyboardButton(text='❔ Información'),
        KeyboardButton(text='🔚 Salir de la enfermería')])
    return reply_kb