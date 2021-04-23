from flask import Flask, json, jsonify, Response
from flask_restful import Resource, Api, marshal_with, abort, fields
import os
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask import g

db = SQLAlchemy()


resource_fields = {
    'name': fields.String,
    'quality': fields.Integer,
    'sell_in': fields.Integer,
}


class Item(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    quality = db.Column(db.Integer, nullable=False)
    sell_in = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self, name, quality, sell_in):

        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DB_sql:

    inventario = [Item(name="Aged Brie", quality=4, sell_in=3),
                  Item(name="Backstage",
                       quality=6, sell_in=2),
                  Item(name="Sulfuras", quality=0, sell_in=80),
                  Item(name="Conjured Mana Cake", quality=2, sell_in=4),
                  Item(name="Sulfuras", quality=0, sell_in=80),
                  Item(name="Sulfuras", quality=0, sell_in=80), 
                  Item(name="Conjured Mana Cake", quality=3, sell_in=5),
                  Item(name="Aged Brie", quality=7, sell_in=-3)]

    item_1= Item(name="Backstage",
                quality=6, sell_in=2)

    @staticmethod
    def add_items():
        inventario = DB_sql.inventario
        for item in inventario:
            db.session.add(item)
        db.session.commit()

    @staticmethod
    def get_items():
        items = db.session.query(Item).all()
        inventario = []
        for item in items:
            item_json = {'name': item.name, 'sell_in': item.sell_in, 'quality': item.quality}
            inventario.append(item_json)
        return {'items': inventario}

    # @staticmethod
    # def updateQuality():
    #     db = g.db
    #     for item in g.Item.objects():
    #         item_object = Item(
    #             [item.name, item.sell_in, item.quality])
    #         item_object.update_quality()
    #         item.sell_in = item_object.sell_in
    #         item.quality = item_object.quality
    #         item.save()
    #     return Item

    @staticmethod
    def get_item(itemName):
        if not itemName:
            abort(404, description="Es necesario el nombre del item")
        item = Item.query.filter_by(name=itemName).first()
        if not item:
            abort(404, description="El item {} no existe".format(itemName))
        return jsonify(name= item.name, quality=item.quality, sell_in=item.sell_in)

    @staticmethod
    def deleteAllthatMatchName(itemName):
        if not itemName:
            abort(404, description="Es necesario el nombre del item")
        item = db.session.query(Item).filter_by(name=itemName).first()
        if not item:
            abort(404, description="El item {} no existe".format(itemName))
        db.session.query(Item).filter_by(name=itemName).delete()
        db.session.commit()
        return 'Objeto borrado'
