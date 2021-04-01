import logging
import time
import datetime
from contextlib import suppress
from random import choice, randint, uniform

from aiogram.dispatcher import FSMContext
from aiogram.types import (CallbackQuery, KeyboardButton, Message,
                           ReplyKeyboardMarkup)
from aiogram.types.chat import ChatActions
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted, MessageCantBeEdited
from sqlalchemy import and_

from app.__main__ import bot

from ..helpers.keyboards import (IDLE_Kb,MISIONES_kb)




async def user_misiones(m: Message):
    await m.answer(text='🌲Bosque 3min \n Pueden pasar muchas cosas en el bosque.\n'
                        '🗡Foray 🔋🔋 \n'
                        'La incursión es una actividad peligrosa. Alguien puede notarlo y puede golpearlo. Pero si pasas desapercibido, conseguirás mucho botín. \n'
                        '📯Arena \n'
                        'Arena no es un lugar para débiles. Aquí luchas contra otros jugadores y si sales victorioso, adquieres una experiencia preciosa.'
                        , reply_markup=MISIONES_kb())


async def mision_pve(c: CallbackQuery):
    if c.message:
        if c.data == "bosque":
            starttime = time.time()
            i = 1

            await c.message.answer(text='En una necesidad extrema de una aventura, fuiste a un bosque.\n'
                                                            'Regresarás en 3 minutos.', reply_markup=IDLE_Kb())
            
            while (i >= 1):
                time.sleep(180 - ((time.time() - starttime) % 180))                    
                await c.message.answer(text='De repente estabas rodeado por una enorme banda de orcos, liderados por un chamán Orco.\n' 
                                                        'Exigieron que les dieras todo lo que tienes. Mataste a cada uno de ellos y recogiste un montón de botín.\n\n'
                                                        'Usted recibió: 15 exp y 2 oro\n'
                                                        'Ganado: Palo (1)\n'
                                                        'Ganado: Polvo (1)\n')
                break
        
        if c.data == "pantano":
            starttime = time.time()
            i = 1
            await c.message.answer(text='Una aventura está llamando. Pero fuiste a un pantano.\n'
                        'Regresarás en 6 minutos.', reply_markup=IDLE_Kb())  
            while (i >= 1):
                time.sleep(260 - ((time.time() - starttime) % 260))                    
                await c.message.answer(text='un minutos ganaste.')
                break          
        
        if c.data == "valle":
            starttime = time.time()
            i = 1
            await c.message.answer(text='Las montañas pueden ser un lugar peligroso.\nDecidiste investigar, qué está pasando.\n'
                        'Regresarás en 4 minutos.', reply_markup=IDLE_Kb())
            
            while (i >= 1):
                time.sleep(240 - ((time.time() - starttime) % 240))                    
                await c.message.answer(text='un minutos ganaste.')
                break
        
        if c.data == "foray":
            starttime = time.time()
            i = 1
            await c.message.answer(text='Sintiendo una lujuria insatisfactoria por la violencia te diriges al pueblo más cercano.\n'                 
                        'Llegará a la más cercana en 4 minutos.', reply_markup=IDLE_Kb())
            while (i >= 1):
                time.sleep(240 - ((time.time() - starttime) % 240))                    
                await c.message.answer(text='un minutos ganaste.')
                break
        
        if c.data == "arena":
            await c.message.answer(text='📯 Bienvenido a Arena!\n'               
                                                        'El aire sucio está empapado con el espeso olor de la sangre.\n' 
                                                        'Nadie termina aquí por accidente: no puedes irte una vez que comienzas tu batalla.\n' 
                                                        'Espero que tu espada esté afilada y tu escudo firme.\n\n'
                                                        'Su rango: 893\nTus peleas: 0/5\n\n'
                                                        'Clasificación de combate: /top 5\nCrecimiento más rápido: /top 6\n\n'
                                                        'Precio de la entrada: 5 💰', reply_markup=IDLE_Kb())


