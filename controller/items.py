from flask import Flask
from flask_restful import Resource, Api
from services.service import Service



class Items(Resource):

    #/item/<name>

    def get(self, name):
        #curl http://localhost:5000/items/name/"Aged+Brie"
        return Service.get_item(name), 200 #???
