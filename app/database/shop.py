# pylint: skip-file

from .db import db


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True, comment='Operación de identificación única')
    item_id = db.Column(db.Integer, nullable=False, comment='Identificación del artículo vendido')
    item = db.Column(db.String, nullable=False, comment='Artículo vendido')
    rank = db.Column(db.String(1), nullable=False, comment='Rango')
    price = db.Column(db.Integer, nullable=False, comment='Precio del artículo')
    user_id = db.Column(db.Integer, nullable=False, comment='Identificación del vendedor')