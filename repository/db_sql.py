from flask import Flask
from flask_restful import Resource, Api
import os
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask import g

db = SQLAlchemy()

class Inventario(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    object_type = db.Column(db.String(30))
    name = db.Column(db.String(30), nullable=False)
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


