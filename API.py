from flask import Flask
from flask_restful import Resource, Api
import os
from flask_sqlalchemy import SQLAlchemy
from controller.items import Items
from controller.objeto import Objeto
from domain.types import *
from services.service import Service


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pomeranian@localhost/guildedrose"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Inventario(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    object_type = db.Column(db.String(30))
    name = db.Column(db.String(30), nullable=False)
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


db.drop_all()
db.create_all()


class WelcomeOllivanders(Resource):
    def get(self):
        return {"Hello": "Ollivanders"}


api.add_resource(WelcomeOllivanders, "/")
api.add_resource(Items, "/items/<name>")
api.add_resource(Objeto, "/objeto/<name>")


if __name__ == "__main__":
    app.run(debug=True)
