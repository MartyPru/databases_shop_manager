DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq;
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;

CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  quantity int,
  price int
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  order_date text,
  item_id int,
  constraint fk_item foreign key(item_id) references items(id)
  on delete cascade
);

SET datestyle to DMY;

INSERT INTO items (name, quantity, price) VALUES
('Apple Juice', 50, 1),
('Orange Juice', 40, 2),
('Unobtanium Juice', 1, 1000),
('Watermelon Juice', 20, 5),
('Sugar Cane Juice', 10, 7);

INSERT INTO orders (customer_name, order_date, item_id) VALUES
('Miles Quaritch', '30/11/2023', 3),
('Steve', '30/11/2023', 1),
('Dave', '29/11/2023', 4),
('Bobby', '29/11/2023', 1);