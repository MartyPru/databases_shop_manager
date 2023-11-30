from lib.order import *
"""
When initiated with title, release_year, artist_id
Has attributes for each of those values
"""
def test_initial_attributes():
    order = Order(1, 'Steve', '30/10/2023', 2)
    assert order.customer_name == 'Steve'
    assert order.id == 1
    assert order.order_date == '30/10/2023'
    assert order.item_id == 2

"""
When two posts with same information are created
They are equal
"""
def test_equality():
    order_1 = Order(1, 'Steve', '30/10/2023', 2)
    order_2 = Order(1, 'Steve', '30/10/2023', 2)
    assert order_1 == order_2

"""
When formatted into a string
Shows easy-to-read string
"""
def test_str_formatting():
    order = Order(1, 'Steve', '30/10/2023', 2)
    assert str(order) == "Order(1, Steve, 30/10/2023, 2)"