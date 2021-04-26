from repository.db_inicializar import get_DB
from repository.db_models import Item
from flask_restful import abort
from flask.json import jsonify

class Services():
    @staticmethod
    def get_items():
        db = get_DB()
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
        db = get_DB()
        if not itemName:
            abort(404, description="Es necesario el nombre del item")
        item = Item.query.filter_by(name=itemName).first()
        if not item:
            abort(404, description="El item {} no existe".format(itemName))
        return jsonify(name= item.name, quality=item.quality, sell_in=item.sell_in)

    @staticmethod
    def deleteAllthatMatchName(itemName):
        db = get_DB()
        if not itemName:
            abort(404, description="Es necesario el nombre del item")
        item = db.session.query(Item).filter_by(name=itemName).first()
        if not item:
            abort(404, description="El item {} no existe".format(itemName))
        db.session.query(Item).filter_by(name=itemName).delete()
        db.session.commit()
        return 'Objeto borrado'
