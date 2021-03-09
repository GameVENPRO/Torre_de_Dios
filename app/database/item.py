# pylint: skip-file

from .db import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, comment='ID único')
    name = db.Column(db.String, nullable=False, comment='Nombre del artículo')
    attack_boost = db.Column(db.Integer, nullable=False, comment='Aumento de daño')
    defence_boost = db.Column(db.Integer, nullable=False, comment='Mejorar la protecciónы')
    rank = db.Column(db.String, nullable=False, comment='Rango para obtener')
    quality = db.Column(db.String, nullable=False, comment='Calidad')
    item_class = db.Column(db.String, nullable=False, comment='Armas o armaduras')
