class DB():
    inventario = [["Conjured Mana Cake", 2, 4],["Aged Brie", 3, 4], ["Sulfuras", 2, 4], ["Backstage Passes", 2, 6]]

    @staticmethod
    def get_item(name):
        items = DB.inventario
        print(items)
        return [item for item in items if item[0] == name]
