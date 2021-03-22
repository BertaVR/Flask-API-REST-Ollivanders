from flask_restful import fields, abort, marshal_with
from repository.db import DB
import json


class Service():

    # resource_fields = {
    #     'name': fields.String,
    #     'sell_in': fields.Integer,
    #     'quality': fields.Integer
    # }

    @staticmethod
    # @marshal_with(resource_fields)
    def get_item(name):

        if not name:
            abort(406, message="Es necesario el nombre del item")

        items = DB.get_item(name)

        if not items:
            abort(404, message="El item {} no existe".format(name))

        for item in items:
            return {"name": item[0], "sell_in": str(item[1]), "quality": str(item[2])}
