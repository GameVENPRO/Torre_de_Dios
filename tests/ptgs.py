# pylint: skip-file

import asyncio
from gino import Gino
from sqlalchemy import ARRAY

db = Gino()

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
    name = db.Column(db.String, nullable=False, comment='Nombre del artículo')
    attack_boost = db.Column(db.Integer, nullable=False, comment='Aumento de daño')
    defence_boost = db.Column(db.Integer, nullable=False, comment='Mejorar la protección')
    rank = db.Column(db.String, nullable=False, comment='Rango para obtener')
    quality = db.Column(db.String, nullable=False, comment='Calidad')
    item_class = db.Column(db.String, nullable=False, comment='Armas o armaduras')

class Ability(db.Model):
    __tablename__ = 'abilities'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
    name = db.Column(db.String, nullable=False, comment='Título de habilidad')
    func = db.Column(db.String, nullable=False, comment='Función')
    rank = db.Column(db.String(1), nullable=False, comment='Rango para obtener')

class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True, comment='Operación de identificación única')
    item_id = db.Column(db.Integer, nullable=False, comment='Identificación del artículo vendido')
    item = db.Column(db.String, nullable=False, comment='Artículo vendido')
    rank = db.Column(db.String(1), nullable=False, comment='Rango')
    price = db.Column(db.Integer, nullable=False, comment='Precio del artículo')
    user_id = db.Column(db.Integer, nullable=False, comment='Identificación del vendedor')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
    username = db.Column(db.String, nullable=False, server_default='noname', comment='Nombre')
    rank = db.Column(db.String(1), nullable=False, server_default='-', comment='Rango')
    lvl = db.Column(db.Integer, nullable=False, server_default='1', comment='Nivel')
    xp = db.Column(db.Integer, nullable=False, server_default='0', comment='Experiencia')
    damage = db.Column(db.Integer, nullable=False, server_default='3', comment='Daño infligido')
    weapon = db.Column(db.Integer, server_default=None, comment='Armas')
    health = db.Column(db.Integer, nullable=False, server_default='5', comment='Salud')
    max_health = db.Column(db.Integer, nullable=False, server_default='5', comment='Max. Salud')
    defence = db.Column(db.Integer, nullable=False, server_default='5', comment='Protección')
    max_defence = db.Column(db.Integer, nullable=False, server_default='5', comment='Max. Protección')
    armor = db.Column(db.Integer, server_default=None, comment='Armadura')
    level_points = db.Column(db.Integer, nullable=False, server_default='0', comment='Puntos de mejora')
    inventory = db.Column(ARRAY(db.Integer), nullable=False, server_default="{}", comment='Inventario')
    balance = db.Column(db.Integer, nullable=False, server_default='0', comment='Balance')
    heal_potions = db.Column(db.Integer, nullable=False, server_default='1', comment='Poción curativa')
    abilities = db.Column(ARRAY(db.Integer), nullable=False, server_default="{}", comment='Capacidades')

async def main():
    await db.set_bind('postgresql://postgres:123456789@localhost:5432/tower')
    await db.gino.create_all()

    # further code goes here
    item1 = await Item.create(id=40, name='(Ordinario) quirasa el Conquistador', 
                             attack_boost=1, defence_boost=16,rank='B', 
                             quality='Común', item_class='armor')

    item2 = await Item.create(id=41, name='(Raro) kiras el Conquistador', 
                            attack_boost=2, defence_boost=17, rank='B', 
                            quality='Raro', item_class='armor')

    item3 = await Item.create(id=42, name='(Épica) Quirós el Conquistador', 
                            attack_boost=3, defence_boost=19, rank='B', 
                            quality='Épica', item_class='armor')

    item4 = await Item.create(id=43, name='(Legendario) Quirós el Conquistador', 
                            attack_boost=4, defence_boost=21, rank='B', 
                            quality='Legendario', item_class='armor')         

    # WEAPON:

    item5 = await Item.create(id=44, name='(Habitual) Alpargata', 
                             attack_boost=14, defence_boost=3,rank='B', 
                             quality='Común', item_class='weapon')

    item6 = await Item.create(id=45, name='(Raro) Alpargata', 
                            attack_boost=15, defence_boost=4, rank='B', 
                            quality='Raro', item_class='weapon')

    item7 = await Item.create(id=46, name='(Épica) Espadrón', 
                            attack_boost=17, defence_boost=5, rank='B', 
                            quality='Épica', item_class='weapon')

    item8 = await Item.create(id=47, name='(Legendario) Espadrón', 
                            attack_boost=19, defence_boost=6, rank='B', 
                            quality='Arma legendaria', item_class='weapon')                    

    await db.pop_bind().close()


asyncio.get_event_loop().run_until_complete(main())

