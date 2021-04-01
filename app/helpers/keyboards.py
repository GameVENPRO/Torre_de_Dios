import random
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# MAIN KEYBOARDS:
def random_sele():
    tecla_reg = ['🐉Escama de dragon','🌑Luz lunar','🥔Papa','🦅Nido alto','🐺Manada de lobos','🦌Cuerno de ciervo','🦈Dientes de Tiburón']
    tcl = random.sample(tecla_reg , 4)
    return tcl

def REGISTRO_Kb():
    reg_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    reg_kb.add(*[KeyboardButton(name) for name in random_sele()])
    return reg_kb

def IDLE_Kb():
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    main_kb.add(*[KeyboardButton(name) for name in['⚔️Atacar','🗺Misiones','🛡Defender','🏅Yo','🏰Castillo','👥Clanes']])
    return main_kb

def INV_Kb():
    main_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    main_kb.add(*[KeyboardButton(name) for name in['🎒Bolso','📦Recursos','🗃Varios','⚗️Alquimia','⚒Elaboración','🏷Equipamiento','⬅️Atras']])
    return main_kb
#KB Castillo...
def CASTILLO_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['⚒Taller','🍺Taberna','🛎Subasta','🏠Tienda','⚖️Intercambio', '⬅️Atras']])
    return prin_kb
def TALLER_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['⚒Mesa de trabajo','📖Recetas','🏷Envolver', '⬅️Atras']])
    return prin_kb
def MESA_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['⚒Craft','📖Recetas','🏷Envolver', '⬅️Atras']])
    return prin_kb
def TABERNA_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(name) for name in ['🍺Tomar Cervesa','🎲Jugar a los dados','🕵️Hablar con un extraño', '⬅️Atras']])
    return kb

def PASAPORTE_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(name) for name in ['🦈Pasaporte','🐉Pasaporte','🦌Pasaporte','🥔Pasaporte','🐺Pasaporte','🌑Pasaporte','🦅Pasaporte', '⬅️Atras']])
    return kb

def SUBASTA_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(name) for name in ['🍺Tomar Cervesa','📖Recetas','🏷Envolver', '⬅️Atras']])
    return kb
def TIENDA_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(name) for name in ['🍺Tomar Cervesa','📖Recetas','🏷Envolver', '⬅️Atras']])
    return kb
def INTERCAMBIO_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[KeyboardButton(name) for name in ['🍺Tomar Cervesa','📖Recetas','🏷Envolver', '⬅️Atras']])
    return kb
#.......
def GREMIO_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['📦Stock','📋Lista','ℹ️Otros','🏕Misiones','🤝Alianza', '⬅️Atras']])
    return prin_kb

def MISIONES_kb():
    kb = InlineKeyboardMarkup(row_width=3)
    kb.row(InlineKeyboardButton(text="🌲Bosque",   callback_data="bosque"),
            InlineKeyboardButton(text="🍄Pantano", callback_data="pantano"),
            InlineKeyboardButton(text="🏔Valle",   callback_data="valle"),
            InlineKeyboardButton(text="🗡Foray",   callback_data="foray"),
            InlineKeyboardButton(text="📯Arena",   callback_data="arena"))
    return kb

     
def ATCK_DRAGONES_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🌑','🥔','🦅','🐺','🦌','🦈']])
    return admin_kb 
   
def ATCK_LOBO_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🦅','🦌','🦈']])
    return admin_kb 

def ATCK_LUNA_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🥔','🦅','🐺','🦌','🦈']])
    return admin_kb

def ATCK_PAPA_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🦅','🐺','🦌','🦈']])
    return admin_kb

def ATCK_AGULA_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🐺','🦌','🦈']])
    return admin_kb   

def ATCK_CIERVO_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🦅','🐺','🦈']])
    return admin_kb

def ATCK_TUBURON_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🦅','🐺','🦌']])
    return admin_kb

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