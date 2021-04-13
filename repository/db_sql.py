from flask import Flask
from flask_restful import Resource, Api
import os
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask import g

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    object_type = db.Column(db.String(90))
    name = db.Column(db.String(90), nullable=False)
    quality = db.Column(db.Integer, nullable=False)
    sell_in = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self, object_type, name, quality, sell_in):
        self.object_type = object_type
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

class DB_sql:

    inventario = [Item(object_type = "AgedBrie", name = "Aged Brie", quality = 4 , sell_in = 3),
        Item(object_type = "Backstage", name = "Backstage passes to a TAFKAL80ETC concert", quality = 6, sell_in = 2),
        Item(object_type = "Sulfuras", name = "Sulfuras, hand of Ragnaros", quality = 0, sell_in = 80),
        Item(object_type = "NormalItem", name = "Conjured Mana Cake", quality = 2, sell_in = 4),
        Item(object_type = "ConjuredItem", name = "Sulfuras", quality = 0, sell_in = 80)]

    @staticmethod
    def add_items(self):
        inventario = DB_sql.inventario
        for item in inventario:
            db.session.add(item)         
        db.session.commit()

  

    @staticmethod
    def delete_item( name, quality, sell_in):
        Item.query.filter_by( name = name, quality = quality, sell_in = sell_in).delete()
        db.session.commit()


    
    

