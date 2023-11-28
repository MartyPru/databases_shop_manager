-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS accounts CASCADE;
DROP SEQUENCE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  username varchar(255),
  email_address varchar(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title varchar(255),
  content text,
  views int,
  account_id int,
  constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO accounts (username, email_address) VALUES ('user1', 'user1@network.com');
INSERT INTO accounts (username, email_address) VALUES ('user2', 'user2@network.com');
INSERT INTO accounts (username, email_address) VALUES ('user3', 'user3@network.com');
INSERT INTO accounts (username, email_address) VALUES ('user4', 'user4@network.com');


INSERT INTO posts (title, content, views, account_id) VALUES ('Title 1', 'This is Content 1', 100, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title 2', 'This is Content 2', 200, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title 3', 'This is Content 3', 300, 3);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title 4', 'This is Content 4', 100, 4);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title 5', 'This is Content 5', 150, 2);


