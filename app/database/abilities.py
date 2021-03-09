# pylint: skip-file

from .db import db


class Ability(db.Model):
    __tablename__ = 'abilities'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
    name = db.Column(db.String, nullable=False, comment='Título de habilidad')
    func = db.Column(db.String, nullable=False, comment='Función')
    rank = db.Column(db.String(1), nullable=False, comment='Rango para obtener')
