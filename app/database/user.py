# pylint: skip-file

from sqlalchemy import ARRAY
from .db import db


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

    # inventory = db.Column(ARRAY(db.Integer), nullable=False, server_default="{}", comment='Inventario')
