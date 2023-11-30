from lib.order_repository import OrderRepository
from lib.order import Order

def test_create_and_find_all(db_connection):
    db_connection.seed('seeds/shop_manager.sql')
    repo = OrderRepository(db_connection)
    order_1 = Order(None, 'Steve', '30/10/2023', 2)
    order_2 = Order(None, 'Lucy', '30/10/2023', 1)
    repo.create_order(order_1)
    repo.create_order(order_2)
    orders = repo.all()
    assert orders == [
        Order(1, 'Miles Quaritch', '30/11/2023', 3),
        Order(2, 'Steve', '30/11/2023', 1),
        Order(3, 'Dave', '29/11/2023', 4),
        Order(4, 'Bobby', '29/11/2023', 1),
        Order(5, 'Steve', '30/10/2023', 2),
        Order(6, 'Lucy', '30/10/2023', 1)
    ]