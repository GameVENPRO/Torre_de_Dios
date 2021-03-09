import logging
from contextlib import suppress
from math import fabs

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.utils.exceptions import (MessageToDeleteNotFound,
                                      MessageToEditNotFound)

from app.__main__ import bot

from ..database.base import Item, Shop, User
from ..handlers.user_handlers import user_inventory
from ..helpers.dev_text import gear_info_text
from ..helpers.keyboards import (CONFIRM_Kb, CRAFT_Kb, EQUIPMENT_Kb, IDLE_Kb,
                                 UNDRESS_Kb)
from ..utils.states import MainStates


async def gear_info_check(m: Message):
    try:
        gear = await Item.get(int(m.text[1:]))
        if gear:
            await m.answer(text=gear_info_text(gear))
        else:
            with suppress(MessageToDeleteNotFound):
                await m.delete()
            await m.answer('❗ Tal objeto no existe') 
    except ValueError:
        return
    


async def gear_equip(c: CallbackQuery, user: User):
    if c.data[6:] == 'back':
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await user_inventory(c.message, user)
    else:
        gear = await Item.get(int(c.data[6:]))
        if gear.id in user.inventory:
            if getattr(user, gear.item_class) is None:
                user.inventory.remove(gear.id)
                await user.update(inventory=user.inventory, defence=user.defence + gear.defence_boost,
                                max_defence=user.max_defence + gear.defence_boost, 
                                damage=user.damage + gear.attack_boost).apply()
                
                await user.update(weapon=gear.id).apply() if gear.item_class == 'weapon' else await user.update(armor=gear.id).apply()
                    
                await c.message.delete()
                await c.message.answer(text="❕ Te has puesto el equipo.", reply_markup=IDLE_Kb())
            else:
                await c.message.delete()
                await c.message.answer(text="❗ Retire el equipo primero", reply_markup=EQUIPMENT_Kb())
        else:
            await c.message.delete()
            await c.message.answer(text="❗ Usted no tiene tal artículo", reply_markup=IDLE_Kb())
    


async def gear_unequip(m: Message, user: User):
    if (user.weapon or user.armor) != None:
        eq = [user.weapon, user.armor]
        data = []
        for i in range(len(eq)):
            if eq[i] != None:
                gear = await Item.get(eq[i])
                data.extend([gear.name, gear.id])
            else:
                data.extend(['- Está vacío -', 'empty'])
        await m.answer('❔ Elige qué equipo disparar:',
                       reply_markup=UNDRESS_Kb(data))
    else:
        await m.answer('❗ No tienes equipo.', reply_markup=IDLE_Kb())


async def gear_unequip_query(c: CallbackQuery, user: User):
    gear = await Item.get(int(c.data[8:]))
    # user.weapon => Common Sword (example)
    if gear:
        user.inventory.append(gear.id)
        await user.update(defence=user.defence - gear.defence_boost if user.defence - gear.defence_boost >= 0 else 0, 
                          max_defence=user.max_defence - gear.defence_boost,
                          damage=user.damage - gear.attack_boost, inventory=user.inventory).apply()
        await user.update(weapon=None).apply() if gear.item_class == 'weapon' else await user.update(armor=None).apply()

        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await c.message.answer(f"❕ Usted filmó \"{gear.name}\"", reply_markup=IDLE_Kb())
    else:
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await c.message.answer('❗ No tienes equipo.', reply_markup=IDLE_Kb())


async def gear_craft(m: Message, user: User):
    raw = []
    if user.inventory:
        inv = dict((x, int(user.inventory.count(x) / 2)) for x in set(user.inventory) if user.inventory.count(x) != 1)
        if inv:
            for x, y in inv.items():
                raw_items = await Item.get(int(x))
                if raw_items:
                    for _ in range(y):
                        raw.append(raw_items)
            print(inv, '|', raw_items, '|', raw)
            await m.answer(text='🧳❕ Elija qué par de artículos para elaborar:', reply_markup=CRAFT_Kb(raw))
        else:
            await m.answer(text='❗ No tienes los artículos adecuados', reply_markup=IDLE_Kb())
    else:
        await m.answer(text='❗ Inventario vacío', reply_markup=IDLE_Kb())


async def gear_craft_query(c: CallbackQuery, user: User):
    curr_gear = await Item.get(int(c.data[6:]))
    if curr_gear:
        for _ in range(2):
            if curr_gear.id in user.inventory:
                user.inventory.remove(curr_gear.id)
            else:
                with suppress(MessageToDeleteNotFound):
                    await c.message.delete()
                await c.message.answer('❕ Ya no hay tal artículo en su inventario', reply_markup=IDLE_Kb())
                return

        craft_result = await Item.get(curr_gear.id + 1)
        if curr_gear.item_class == craft_result.item_class:
            user.inventory.append(craft_result.id)
            await user.update(inventory=user.inventory).apply()
            with suppress(MessageToDeleteNotFound):
                await c.message.delete()
            await c.message.answer(
                text=f"❕ Has creado con éxito el artículo:\n\n{gear_info_text(craft_result)}",
                reply_markup=IDLE_Kb())
        else:
            with suppress(MessageToDeleteNotFound):
                await c.message.delete()
            await c.message.answer('❗ Artículos ya de máxima calidad', reply_markup=IDLE_Kb())
    else:
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await c.message.answer('<b>Error:</b> Broken item (Póngase en contacto con el establecimiento)', reply_markup=IDLE_Kb())
        raise NameError("Broken item")


async def gear_sell_confirm(c: CallbackQuery, user: User):
    await c.message.edit_text(f'💸 <b>Venta de artículos.</b>\n\n<i>  - La venta del artículo se realiza entre los jugadores, sin la participación de la administración. Sugerir poner un precio razonable\n\n'
                              f'  - La venta de un artículo que no obtendrá un beneficio<u>en un momento</u>! Sólo lo registra.\"a la cola\" donde otros usuarios pueden comprarlo.</i>',
                              reply_markup=CONFIRM_Kb(text=('💸 Continuar', '🔚 Cancelar'), callback=f'sell_register_{c.data[5:]}'))



async def gear_sell_register(c: CallbackQuery, user: User, state: FSMContext):
    item = await Item.get(int(c.data[14:]))
    if item: 
        await MainStates.selling.set()
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        trash = await c.message.answer('❔ <b>Cómo registrar un artículo:</b>\n\n<i>  - En esta etapa, todo es simple porque la Torre hace casi todo por TI, '
                                       'tienes que enviar el bot <u>costo</u> objeto</i>. \n\nEjemplo: '
                                       '\"999\"', reply_markup=ReplyKeyboardRemove())
        async with state.proxy() as data:
            data['sell_item'] = item
            data['trash'] = trash
    else:
        with suppress(MessageToDeleteNotFound):
            await c.message.delete()
        await c.message.answer('<b>Error:</b> Broken item (Póngase en contacto con el establecimiento)', reply_markup=IDLE_Kb())
        raise NameError("Broken item")


async def gear_sell_registered(m: Message, user: User, state: FSMContext):
    async with state.proxy() as data:
        item = data['sell_item']
        trash = data['trash']
    try:
        request = await Shop.create(item_id=item.id, item=item.name, rank=item.rank, price=int(fabs(int(m.text))), user_id=user.id)
        # removing from the inventory
        user.inventory.remove(request.item_id)
        await m.delete()
        with suppress(MessageToDeleteNotFound):
            await trash.delete()
            await m.answer(text=f'❕ Lote №{request.id} en venta creado:\n\n{request.item}: /{request.item_id}\n'
                                f'🏆 Grado del objeto: {request.rank}\n💸 Precio: {request.price}', reply_markup=IDLE_Kb())
        await user.update(inventory=user.inventory).apply()
    except (ValueError):
        await m.delete()
        with suppress(MessageToDeleteNotFound):
            await trash.delete()
            await m.answer(text='❗️ No ha introducido un número.', reply_markup=IDLE_Kb())
    finally:
        await state.reset_data()
        await state.reset_state()
