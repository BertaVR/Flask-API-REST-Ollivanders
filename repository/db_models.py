from repository.db_conexion import db

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
