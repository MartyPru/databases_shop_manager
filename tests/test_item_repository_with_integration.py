from lib.item import Item
from lib.item_repository import ItemRepository

def test_create_and_find_all(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repo = ItemRepository(db_connection)
    item_1 = Item(None, 'Peach Juice', 10, 2)
    item_2 = Item(None, 'Grape Juice', 15, 1)
    repo.create_item(item_1)
    repo.create_item(item_2)
    items = repo.all()
    assert items == [
        Item(1, 'Apple Juice', 50, 1),
        Item(2, 'Orange Juice', 40, 2),
        Item(3, 'Unobtanium Juice', 1, 1000),
        Item(4, 'Watermelon Juice', 20, 5),
        Item(5, 'Sugar Cane Juice', 10, 7),
        Item(6, 'Peach Juice', 10, 2),
        Item(7, 'Grape Juice', 15, 1)
    ]