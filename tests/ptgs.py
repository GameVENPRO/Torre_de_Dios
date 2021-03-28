# pylint: skip-file

import asyncio
from gino import Gino
from sqlalchemy import ARRAY

db = Gino()

# class Item(db.Model):
#     __tablename__ = 'items'

#     id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
#     name = db.Column(db.String, nullable=False, comment='Nombre del artículo')
#     attack_boost = db.Column(db.Integer, nullable=False, comment='Aumento de daño')
#     defence_boost = db.Column(db.Integer, nullable=False, comment='Mejorar la protección')
#     rank = db.Column(db.String, nullable=False, comment='Rango para obtener')
#     quality = db.Column(db.String, nullable=False, comment='Calidad')
#     item_class = db.Column(db.String, nullable=False, comment='Armas o armaduras')

# class Ability(db.Model):
#     __tablename__ = 'abilities'

#     id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
#     name = db.Column(db.String, nullable=False, comment='Título de habilidad')
#     func = db.Column(db.String, nullable=False, comment='Función')
#     rank = db.Column(db.String(1), nullable=False, comment='Rango para obtener')

# class Shop(db.Model):
#     __tablename__ = 'shop'

#     id = db.Column(db.Integer, primary_key=True, comment='Operación de identificación única')
#     item_id = db.Column(db.Integer, nullable=False, comment='Identificación del artículo vendido')
#     item = db.Column(db.String, nullable=False, comment='Artículo vendido')
#     rank = db.Column(db.String(1), nullable=False, comment='Rango')
#     price = db.Column(db.Integer, nullable=False, comment='Precio del artículo')
#     user_id = db.Column(db.Integer, nullable=False, comment='Identificación del vendedor')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
    username = db.Column(db.String, nullable=False, server_default='noname', comment='Nombre')
    heroflag = db.Column(db.String, nullable=False, server_default='noname', comment='Bandera')
    castlename = db.Column(db.String, nullable=False, server_default='noname', comment='Castillo')
    heroname = db.Column(db.String, nullable=False, server_default='noname', comment='Nombre de heroe')
    guild = db.Column(db.String, nullable=False, server_default='noname', comment='Clan')
    lvl = db.Column(db.Integer, nullable=False, server_default='1', comment='Nivel')
    xp = db.Column(db.Integer, nullable=False, server_default='0', comment='Experiencia')
    stamina = db.Column(db.Integer, nullable=False, server_default='5', comment='Resistenia')
    stamina_max = db.Column(db.Integer, nullable=False, server_default='5', comment='Resistenia max')
    libros_exp = db.Column(db.Integer, nullable=False, server_default='5', comment='Resistenia')
    oro = db.Column(db.Integer, nullable=False, server_default='1', comment='Oro')
    bolsa_de_oro = db.Column(db.Integer, nullable=False, server_default='0', comment='Bolsa de oro')
    gemas = db.Column(db.Integer, nullable=False, server_default='0', comment='Gemas')
    vida = db.Column(db.Integer, nullable=False, server_default='300', comment='Salud')
    max_vida = db.Column(db.Integer, nullable=False, server_default='300', comment='Max. Salud')
    mana = db.Column(db.Integer, nullable=False, server_default='0', comment='Salud')
    max_mana = db.Column(db.Integer, nullable=False, server_default='0', comment='Max. Salud')
    ataque = db.Column(db.Integer, nullable=False, server_default='1', comment='Ataque del Heroe')
    defensa = db.Column(db.Integer, nullable=False, server_default='1', comment='Defensa del Heroe')
    wins = db.Column(db.String, nullable=False, server_default='0', comment='Nombre')
    arma_p = db.Column(db.Integer, server_default=None, comment='Arma Principal')
    arma_s = db.Column(db.Integer, server_default=None, comment='Arma Segundaria')
    caso = db.Column(db.Integer, server_default=None, comment='Caso')
    guantes = db.Column(db.Integer, server_default=None, comment='Guantes')
    armadura = db.Column(db.Integer, server_default=None, comment='Armaduras')
    botas = db.Column(db.Integer, server_default=None, comment='Botas')
    especial = db.Column(db.Integer, server_default=None, comment='Objetos especiales')
    anillo = db.Column(db.Integer, server_default=None, comment='Anillos')
    collar = db.Column(db.Integer, server_default=None, comment='Collares')
    level_points = db.Column(db.Integer, nullable=False, server_default='0', comment='Puntos de mejora')
    bolso = db.Column(db.Integer, server_default='15', comment='Bolso')
    stock = db.Column(db.Integer, server_default='4000', comment='Stock de recuros')
    mascota = db.Column(db.String, nullable=False, server_default='noname', comment='Mascota')
    clase = db.Column(db.String, nullable=False, server_default='noname', comment='Clase de personaje')
    estado = db.Column(db.String, nullable=False, server_default='🛌Descanso', comment='Estado del personaje') 
    
async def main():
    await db.set_bind('postgresql://postgres:123456789@localhost:5432/tower')
    await db.gino.create_all()

    # # further code goes here
    # item1 = await Item.create(id=40, name='(Ordinario) quirasa el Conquistador', 
    #                          attack_boost=1, defence_boost=16,rank='B', 
    #                          quality='Común', item_class='armor')

    # item2 = await Item.create(id=41, name='(Raro) kiras el Conquistador', 
    #                         attack_boost=2, defence_boost=17, rank='B', 
    #                         quality='Raro', item_class='armor')

    # item3 = await Item.create(id=42, name='(Épica) Quirós el Conquistador', 
    #                         attack_boost=3, defence_boost=19, rank='B', 
    #                         quality='Épica', item_class='armor')

    # item4 = await Item.create(id=43, name='(Legendario) Quirós el Conquistador', 
    #                         attack_boost=4, defence_boost=21, rank='B', 
    #                         quality='Legendario', item_class='armor')         

    # # WEAPON:

    # item5 = await Item.create(id=44, name='(Habitual) Alpargata', 
    #                          attack_boost=14, defence_boost=3,rank='B', 
    #                          quality='Común', item_class='weapon')

    # item6 = await Item.create(id=45, name='(Raro) Alpargata', 
    #                         attack_boost=15, defence_boost=4, rank='B', 
    #                         quality='Raro', item_class='weapon')

    # item7 = await Item.create(id=46, name='(Épica) Espadrón', 
    #                         attack_boost=17, defence_boost=5, rank='B', 
    #                         quality='Épica', item_class='weapon')

    # item8 = await Item.create(id=47, name='(Legendario) Espadrón', 
    #                         attack_boost=19, defence_boost=6, rank='B', 
    #                         quality='Arma legendaria', item_class='weapon')                    

    await db.pop_bind().close()


asyncio.get_event_loop().run_until_complete(main())

