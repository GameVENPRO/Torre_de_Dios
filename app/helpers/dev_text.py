from app.utils.game_logic import power, get_xp
from .scenario import ABILITIES


def user_text(user, username, boost, equipment):
    return (f"Jugador: {username} ({user.xp}/{get_xp(user.lvl)})\n"
            f"🎖 Nivel: {user.lvl} ({user.level_points})\n"
            f"💉 Pociones curativas: {user.heal_potions}\n\n"
            f"🗡 Daño: {user.damage} "
            f"(+{boost[0] + boost[2] if boost is not None else 0})\n"
            f"♥ Salud: <b>{user.health}</b>/{user.max_health}\n"
            f"🛡️ Protección: <b>{user.defence}</b>/{user.max_defence} "
            f"(+{boost[1] + boost[3] if boost is not None else 0})\n\n"
            f"🔪 Armas: {'-' if user.weapon is None else ' /'.join((equipment[0].split(' ', 1)[1], str(user.weapon)))}\n"
            f"🥋 Armadura: {'-' if user.armor is None else ' /'.join((equipment[1].split(' ', 1)[1], str(user.armor)))}\n"
            f"💼 Inventario: {len(user.inventory) if user.inventory else 0}\n\n"
            f"⚜ Fuerza: <b>{power(user)}</b>/{power(user, maximal=True)}\n"
            f"💰 Balance: {user.balance}\n"
            f"🏆 Rango: {user.rank}")


def meet_enemy_text(enemy, difficulty):
    return (f"Has conocido <b>{enemy.name}</b>:\n\n"
            f"⭐ Experiencia por asesinato: {enemy.bonus}\n"   
            f"💰 Dinero por asesinato: {enemy.bonus//2}\n\n"
            f"🗡 Daño: {enemy.damage}\n"
            f"♥ Salud: {enemy.health}\n"
            f"🛡 Protección: {enemy.defence}\n\n"
            f"🎲 Oportunidad de Drop: {enemy.drop_chance}%\n"
            f"‼ Complejidad: <b>{difficulty}</b> (⚜️<b>{power(enemy)}</b>)")


def rankup_text(enemy, user, difficulty):
    return (f"<b>Su rango actual: \"{user.rank}\":</b>\n"
            f"Tu examinador: <b>{enemy.name}</b>:\n\n"
            f"🗡 Daño: {enemy.damage}\n"
            f"♥ Salud: {enemy.health}\n"
            f"🛡 Protección: {enemy.defence}\n\n"
            f"🏆 Rango: {enemy.rank}\n"
            f"‼ Complejidad: {difficulty} (<b>{enemy.power}</b>)")


def gear_info_text(gear):
    return (f"{gear.name}:\n"
            f"+🗡 Aumento de ataque: {gear.attack_boost}\n"
            f"+🛡 Mejorar la protección: {gear.defence_boost}\n"
            f"🏆 Grado del objeto: {gear.rank}\n"
            f"🎗 Destino: {'Armas' if gear.item_class == 'weapon' else 'Armadura'}\n"
            f"💠 Calidad: {gear.quality}")


def ability_info_text(ability):
    return (f"🎲 <b>{ability.name}</b>:\n\n"
            f"❔ <i>\"{ABILITIES.get(ability.id)}\"</i>\n\n"
            f"🏆 Grado de la capacidad: {ability.rank}\n")


def lvl_up_text(bonus, points):
    return (f"🎊 Usted recibió +{bonus}<i>XP</i>, y su nivel es elevado! "
            f"В ¡las conexiones con las que se trasladaron al siguiente piso!!\n"
            f"<i>Usted cuenta ({points}) puntos de mejora.</i>")
