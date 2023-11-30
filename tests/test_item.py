from lib.item import *
"""
When initiated with title, release_year, artist_id
Has attributes for each of those values
"""
def test_initial_attributes():
    item = Item(1, 'Apple Juice', 10, 2)
    assert item.id == 1
    assert item.name == 'Apple Juice'
    assert item.quantity == 10
    assert item.price == 2

"""
When two posts with same information are created
They are equal
"""
def test_equality():
    item_1 = Item(1, 'Apple Juice', 10, 2)
    item_2 = Item(1, 'Apple Juice', 10, 2)
    assert item_1 == item_2

"""
When formatted into a string
Shows easy-to-read string
"""
def test_str_formatting():
    item = Item(1, 'Apple Juice', 10, 2)
    assert str(item) == "Item(1, Apple Juice, 10, 2)"