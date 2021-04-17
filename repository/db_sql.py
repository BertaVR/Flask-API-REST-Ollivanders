from flask import Flask, json, jsonify
from flask_restful import Resource, Api, marshal_with, abort, fields
import os
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask import g

db = SQLAlchemy()


resource_fields = {
    'object_type': fields.String,
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
                  Item(name="Backstage passes to a TAFKAL80ETC concert",
                       quality=6, sell_in=2),
                  Item(name="Sulfuras, hand of Ragnaros", quality=0, sell_in=80),
                  Item(name="Conjured Mana Cake", quality=2, sell_in=4),
                  Item(name="Sulfuras", quality=0, sell_in=80)]

    hola = Item(name="Backstage passes to a TAFKAL80ETC concert",
                quality=6, sell_in=2)

    @staticmethod
    def add_items():
        inventario = DB_sql.inventario
        for item in inventario:
            db.session.add(item)
        db.session.commit()

    @staticmethod
    def get_items():
        items = Item.query.all()
        for item in items:
            return jsonify(name=item.name, quality=item.quality, sell_in=item.sell_in)

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
        items = Item.objects(name=itemName)
        if not items:
            abort(404, message="El item {} no existe".format(itemName))
        return [item for item in items if item[0] == itemName]

    @staticmethod
    def delete_item(name, quality, sell_in):
        Item.query.filter_by(name=name, quality=quality,
                             sell_in=sell_in).delete()
        db.session.commit()
