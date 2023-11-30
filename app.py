# file: app.py

from lib.order_repository import OrderRepository
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order import Order
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/shop_manager.sql")

  def run(self):
    print("Welcome to the shop management program! \n\n")
    print("What would you like to do? \n")
    print("    1 = List all shop items\n")
    print("    2 = Create a new item\n")
    print("    3 = List all orders\n")
    print("    4 = Create a new order\n")
    user_input = input("\n Enter your choice: ")

    if user_input == str(1):
       repo = ItemRepository(self._connection)
       items = repo.all()
       for item in items:
          print(f"* {item.name} - Unit price: {item.price} - Quantity: {item.quantity} \n")
    elif user_input == str(2):
       repo = ItemRepository(self._connection)
       item_name = input("\n Please provide item name (text): ")
       item_quantity = input("\n Please provide item quantity (integer): ")
       item_price = input("\n Please provide item unit price (integer): ")
       item_to_create = Item(None, item_name, item_quantity, item_price)
       repo.create_item(item_to_create)
       print("\n Item has been created :)")
       self.run()
    elif user_input == str(3):
       repo = OrderRepository(self._connection)
       orders = repo.all()
       for order in orders:
          print(f"* Customer: {order.customer_name} - Order Date: {order.order_date} - Item Ordered (Item ID): {order.item_id} \n")
    elif user_input == str(4):
       repo = OrderRepository(self._connection)
       customer_name = input("\n Please provide customer name (text): ")
       order_date = input("\n Please provide order date (text): ")
       item_id = input("\n Please provide item id (integer): ")
       order_to_create = Order(None, customer_name, order_date, item_id)
       repo.create_order(order_to_create)
       print("\n Order has been created :)")
       self.run()


if __name__ == '__main__':
    app = Application()
    app.run()