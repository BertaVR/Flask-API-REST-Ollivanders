from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from controller.items import Items
from controller.objeto import Objeto
from domain.types import *
from services.service import Service


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pomeranian@3306/guildedrose"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Domain(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(64), unique=False)
    name = db.Column(db.String(64), unique=False)
    sell_in = db.Column(db.Integer, unique=False)

    quality = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Domain %r>' % self.name


class WelcomeOllivanders(Resource):
    def get(self):
        return {"Hello": "Ollivanders"}


api.add_resource(WelcomeOllivanders, "/")
api.add_resource(Items, "/items/<name>")
api.add_resource(Objeto, "/objeto/<name>")


if __name__ == "__main__":
    app.run(debug=True)
