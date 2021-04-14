from flask import Flask, request, flash, redirect, url_for, g
from flask_restful import Resource, Api
import os
from flask_sqlalchemy import SQLAlchemy
from controller.items import Items
from controller.objeto import Objeto
from repository.db_sql import Item, db, DB_sql


app = Flask(__name__)
api = Api(app)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pomeranian@localhost/guildedrose"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/create')
def crear_db():
   base_datos = DB_sql()
   db.drop_all()
   db.create_all()
   base_datos.add_objetos()
   return 'Los datos han sido introducidos.'

# @app.route('/delete/')
# def delete(self):
#     DB_sql.delete_item()

@app.route('/items/name/<itemName>')
def get_item(itemName):
    base_datos = DB_sql()
    base_datos.get_item(itemName)


class WelcomeOllivanders(Resource):
    def get(self):
        return {"Hello": "Ollivanders"}


api.add_resource(WelcomeOllivanders, "/")
api.add_resource(Items, "/items/<name>")
api.add_resource(Objeto, "/objeto/<name>")

if __name__ == "__main__":
    app.run(debug=True)
