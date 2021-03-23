from domain.types import AgedBrie, NormalItem

class DB():
    inventario = [["Conjured Mana Cake", 2, 4],["Aged Brie", 3, 4], ["Sulfuras", 2, 4], ["Backstage Passes", 2, 6]]

    objetos = [[AgedBrie("Aged Brie", 3, 4)]]

    @staticmethod
    def get_item(name):
        items = DB.inventario
        print(items)
        return [item for item in items if item[0] == name]

    @classmethod
    def get_objeto(cls, name):
        items = cls.objetos
        return [item for item in items if item.name == name][0]
