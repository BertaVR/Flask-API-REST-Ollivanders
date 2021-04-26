from flask import Flask, json, jsonify, Response
from flask_restful import Resource, Api, marshal_with, abort, fields
import os
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask import g
from repository.db_models import Item


resource_fields = {
    'name': fields.String,
    'quality': fields.Integer,
    'sell_in': fields.Integer,
}

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