from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM items")
        items = []
        for row in rows:
            item = Item(row['id'], row['name'], row['quantity'], row['price'])
            items.append(item)
        return items
    
    def create_item(self, item):
        self.connection.execute("INSERT INTO items (name, quantity, price) \
                                VALUES (%s, %s, %s)",
                                [item.name, item.quantity, item.price])