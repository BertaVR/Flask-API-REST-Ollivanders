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
class DB:
    
    def add_objetos(self):
        aged_brie = Item(object_type = "AgedBrie", name = "Aged Brie", quality = 4 , sell_in = 3)
        backstage = Item(object_type = "Backstage", name = "Backstage passes to a TAFKAL80ETC concert", quality = 6, sell_in = 2)
        sulfuras = Item(object_type = "Sulfuras", name = "Sulfuras, hand of Ragnaros", quality = 0, sell_in = 80)
        conjured_mana_cake = Item(object_type = "NormalItem", name = "Conjured Mana Cake", quality = 2, sell_in = 4)
        conjured_sulfuras = Item(object_type = "ConjuredItem", name = "Sulfuras", quality = 0, sell_in = 80)

        db.session.add(aged_brie)
        db.session.add(backstage)
        db.session.add(sulfuras)
        db.session.add(conjured_mana_cake)
        db.session.add(conjured_sulfuras)

        db.session.commit()





    @staticmethod
    def get_item(name):
        items = DB.inventario
        print(items)
        return [item for item in items if item[0] == name]

    @classmethod
    def get_objeto(cls, name):
        items = cls.objetos
        return [item for item in items if item.name == name][0]

