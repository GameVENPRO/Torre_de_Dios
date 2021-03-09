import logging
from contextlib import suppress
from datetime import datetime, timezone

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import MessageToDeleteNotFound

from ..database.base import Item, User, Ability
from ..helpers.dev_text import gear_info_text, user_text, ability_info_text
from ..helpers.keyboards import (CONFIRM_Kb, INVENTORY_ITEM_Kb, EQUIPMENT_Kb,
                                 HEAL_CONFIRM_Kb, HEAL_PURCHASE_Kb, HEALING_Kb,
                                 HEALING_STATE_Kb, IDLE_Kb, INVENTORY_Kb,
                                 PROFILE_Kb, UPDATE_STATS_Kb, ABILITIES_Kb, ABILITIES_ITEM_Kb)
from ..helpers.scenario import healing_text, what_is_healing
from ..utils.scheduler import scheduler
from ..utils.states import MainStates


async def user_profile(m: Message, user: User, clean=True):
    boost, equipment = [], []
    if (user.weapon or user.armor) is not None:
        eq = [user.weapon, user.armor]
        for i in range(len(eq)):
            if eq[i] is not None:
                gear = await Item.get(eq[i])
                equipment.append(gear.name)
                boost.extend([gear.attack_boost, gear.defence_boost])
            else:
                equipment.append(None)
                boost.extend([0, 0])
    else:
        boost = None
    await m.answer(text=user_text(user, user.username, boost, equipment),
                   reply_markup=PROFILE_Kb() if clean is True else IDLE_Kb())


async def user_inventory(m: Message, user: User):
    if user.inventory:
        formatted = []
        for x in user.inventory:
            raw_item = await Item.get(x)
            if raw_item:
                formatted.append(raw_item)
        await m.answer(text='🧳 Contenido del inventario:', reply_markup=INVENTORY_Kb(formatted))
    else:
        await m.answer(text='❗ Inventario vacío')


async def user_inventory_items(c: CallbackQuery):
    gear = await Item.get(int(c.data[4:]))
    if gear:
        await c.message.edit_text(text=gear_info_text(gear), reply_markup=INVENTORY_ITEM_Kb(gear.id))
    else:
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await c.message.answer('<b>Error:</b> Broken item | Póngase en contacto con el establecimiento')
        logging.error(f"Broken item \"{c.data[4:]}\", {c.from_user.id}")



async def user_equipment(m: Message):
    await m.answer('❕ Seleccione una acción:', reply_markup=EQUIPMENT_Kb())


async def user_healing_options(m: Message):
    await m.answer('❕ Seleccione una acción:', reply_markup=HEALING_Kb())


async def user_healing(m: Message):
    await m.answer(what_is_healing, reply_markup=CONFIRM_Kb(text=('💊 Sí', '🔚 Cerrar'), callback='enter_healing'))


async def user_heal_scheduler(user: User, call: CallbackQuery, state: FSMContext):
    if user.max_defence > user.defence:
        await user.update(defence=user.defence+1).apply()
        await call.message.answer(f'🛎 +1 Protección restaurada {user.defence}/{user.max_defence}', disable_notification=True)
    elif user.max_health > user.health:
        await user.update(health=user.health+1).apply()
        if user.max_health > user.health:
            await call.message.answer(f'🛎 +1 Salud restaurada {user.health}/{user.max_health}', disable_notification=True)
    
    if user.max_health == user.health and user.max_defence == user.defence:
        async with state.proxy() as data:
            raw_time = datetime.now() - data['healing_time']
        time = str(raw_time).split('.')
        await call.message.answer(f'🛎 ¡Estás completamente recuperado! \nTiempo total de estancia - {time[0]}',
                                    reply_markup=IDLE_Kb())
        
        scheduler.remove_job(str(user.id))
        await state.reset_state()
        await state.reset_data()


async def user_healing_query(c: CallbackQuery, user: User, state: FSMContext):
    await MainStates.healing.set()
    async with state.proxy() as data:
        data['healing_time'] = datetime.now()
    scheduler.add_job(user_heal_scheduler, 'interval', minutes=5, id=str(user.id), args=(user, c, state))
    with suppress(MessageToDeleteNotFound):
        await c.message.delete()
    await c.message.answer(text=healing_text, reply_markup=HEALING_STATE_Kb())


async def user_healing_info(m: Message, user: User, state: FSMContext):
    job = scheduler.get_job(str(user.id))
    async with state.proxy() as data:
        raw_time = datetime.now() - data['healing_time']
        time_delta = job.next_run_time - datetime.now(timezone.utc)
    
    healing_time = str(raw_time).split('.')
    next_run_time = str(time_delta).split('.')

    await m.answer(f'🕓 Tiempo para el rastro. regeneración: {next_run_time[0]}\n  - Tiempo de estancia en la enfermería: {healing_time[0]}\n')


async def user_healing_cancel(m: Message, user: User, state: FSMContext):
    async with state.proxy() as data:
        raw_time = datetime.now() - data['healing_time']
    time = str(raw_time).split('.')
    
    await state.reset_state()
    await state.reset_data()
    
    scheduler.remove_job(str(user.id))
    await m.answer(f'❕ Dejó la enfermería. Después de haber estado allí {time[0]}', reply_markup=IDLE_Kb())



async def user_heal(m: Message, user: User):
    if user.heal_potions > 0:
        await m.answer(f"❕ ¿Estás seguro de que quieres usar <i>Poción curativa</i>?\n"
                       f"Te queda: <b>{user.heal_potions}</b>шт.", reply_markup=HEAL_CONFIRM_Kb())
    else:
        await m.answer('❗ No tienes pociones curativas.', reply_markup=HEAL_PURCHASE_Kb((user.lvl * 10) // 4))


async def user_heal_query(c: CallbackQuery, user: User):
    if user.heal_potions > 0:
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await user.update(health=user.max_health, defence=user.max_defence, heal_potions=user.heal_potions-1).apply()
        await user_profile(c.message, user, False)
    else:
        await c.message.answer('❗ No tienes pociones curativas.',
                               reply_markup=HEAL_PURCHASE_Kb((user.lvl * 10) // 4))



async def user_stats_increase(m: Message, user: User):
    await m.delete()
    if user.level_points > 0:
        await m.answer(text="¿Qué característica aumentar?", reply_markup=UPDATE_STATS_Kb())
    else:
        await m.answer('❗ ¡No tienes puntos de ascenso!', reply_markup=IDLE_Kb())


async def user_stats_increase_query(c: CallbackQuery, user: User):
    weapon = await Item.get(user.weapon)
    armor = await Item.get(user.armor)
    attack_boost = (weapon.attack_boost if weapon else 0) + (armor.attack_boost if armor else 0)
    if user.level_points > 0:
        if c.data[13:] == 'damage':
            if (user.damage-attack_boost) * 3 <= user.max_health + user.max_defence:
                await user.update(damage=user.damage+1, level_points=user.level_points-1).apply()
                await c.answer(f'❕ Daño aumentado: {user.damage-1}->{user.damage}', show_alert=True)
            else:
                await c.answer('❗ Para mantener el equilibrio, el ataque no debe exceder un tercio de la alforja de salud y protección.', show_alert=True)
        elif c.data[13:] == 'health':
            await user.update(max_health=user.max_health+1, health=user.health+1, level_points=user.level_points-1).apply()
            await c.answer(f'❕ Salud aumentada: {user.max_health-1}->{user.max_health}', show_alert=True)
        elif c.data[13:] == 'defence':
            await user.update(max_defence=user.max_defence+1, defence=user.defence+1, level_points=user.level_points-1).apply()
            await c.answer(f'❕ Protección aumentada: {user.max_defence-1}->{user.max_defence}', show_alert=True)
    else:
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await user_profile(c.message, user, False)
        await c.answer(text='❗ Has usado todos los puntos de ascenso')


async def user_abilities(m: Message, user: User, clear: bool = True):
    if user.abilities:
        abilities = [await Ability.get(x) for x in user.abilities if await Ability.get(x)]
        if clear:
            await m.answer(text='🎲  Habilidades disponibles:', reply_markup=ABILITIES_Kb(abilities, False))
        else:
            await m.edit_text(text='🎲  Habilidades disponibles:', reply_markup=ABILITIES_Kb(abilities, False))
    else:
        await m.answer(text='❗ No tienes habilidades', reply_markup=IDLE_Kb())


async def user_abilities_query(c: CallbackQuery, user: User):
    if c.data != 'ability_get_back':
        is_clear = False if (c.data[:16] == 'ability_get_atk_' or c.data[:16] == 'ability_get_def_') else True
        ability = await Ability.get(int(c.data[12:] if is_clear else c.data[16:]))
        is_attack = True if c.data[12:15] == 'atk' else False
        await c.message.edit_text(ability_info_text(ability), reply_markup=ABILITIES_ITEM_Kb(clear=is_clear, item=ability.id, attack=is_attack))
    elif c.data == 'ability_get_back':
        await user_abilities(c.message, user, False)