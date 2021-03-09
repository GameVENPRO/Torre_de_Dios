import random
import json
import math


async def battle_attack(x, y, u, e, call):
    if x == y:
        await call.answer("❗ El oponente esquivó el golpe", show_alert=True)
        return e.health, e.defence
    else:
        if e.defence <= 0:
            e.health -= u.damage
            return e.health, e.defence
        else:
            if u.damage > e.defence:
                miss_dmg = u.damage - e.defence
                e.health -= miss_dmg
                e.defence = 0
                return e.health, e.defence
            else:
                e.defence -= u.damage
                return e.health, e.defence


async def battle_defence(x, y, u, e, call):
    if x == y:
        await call.answer("❗ Esquivaste el golpe.", show_alert=True)
        return u.health, u.defence
    else:
        if u.defence <= 0:
            u.health -= e.damage
            return u.health, u.defence
        else:
            if e.damage > u.defence:
                miss_dmg = e.damage - u.defence
                u.health -= miss_dmg
                u.defence = 0
                return u.health, u.defence
            else:
                u.defence -= e.damage
                return u.health, u.defence


def power(obj, maximal=False):
    if maximal is True:
        hp = obj.max_health + obj.max_defence
    else:
        hp = obj.health + obj.defence
    return hp * obj.damage


def exam_choose(user):
    from app.models.examinators import exams
    for i in range(len(exams)):
        if user.rank == '-':
            return exams[0]
        elif exams[i].rank == user.rank:
            try:
                return exams[i + 1]
            except IndexError:
                return 'Rango máximo!'


def set_difficulty(m, u):
    if m * 3 <= u:
        difficulty = 'Och. Es fácil'
    elif m * 2.5 <= u:
        difficulty = 'Es fácil'
    elif m * 2 < u:
        difficulty = 'Normalmente'
    elif m * 1.5 < u:
        difficulty = 'Es complicado'
    elif m < u:
        difficulty = 'Muy difícil'
    elif m > u * 3:
        difficulty = 'Muerte segura'
    elif m >= u:
        difficulty = 'Es imposible'
    else:
        return
    return difficulty


def get_xp(lvl):
    """
    Returns total XP according to gain level
    """
    total_xp = int((lvl * 10) ** 1.1)
    return total_xp * lvl


# def json_inv(u):
#     """
#     Converts string from database to list

#     Example: '[3, 2]' => [3, 2]

#     :param u: User
#     :return: User's inventory as list
#     """
#     inventory = json.loads(u['inventory']) if u['inventory'] != '[]' else []
#     return inventory


def item_drop(chance):
    """
    :param chance: Mob's chance of drop
    :return: True/False
    """
    c = random.randint(1, 100)
    if c <= chance:
        return True
    return False


def round_down(n, decimals=0):
    """
    Rounds a number down to a specified number of digits.

    :param decimals: Specified number of digits
    :param n: Float
    """
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def enemy_calc(u_attack, u_health, u_defence, lvl):
    enemy, result = [], []
    if lvl != 1:
        multiplier = round_down(random.uniform(0.4, 1.1), 1) 
    else:
        multiplier = 0.4
    print(multiplier)
    for stat in (u_attack, u_health, u_defence):
        enemy.append(round(stat*multiplier) if stat != 0 else 0)
        
    e_power = enemy[0]*(enemy[1]+enemy[2])
    formulae = int((e_power/(lvl**1.45))*2)
    result = [enemy, formulae if formulae > 1 else 2]
    
    return result
