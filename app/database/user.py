# pylint: skip-file

from sqlalchemy import ARRAY
from .db import db


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