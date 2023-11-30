DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts;

DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments;


CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  content text,
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

INSERT INTO posts (title, content) VALUES ('Title 1', 'Content 1');
INSERT INTO posts (title, content) VALUES ('Title 2', 'Content 2');
INSERT INTO posts (title, content) VALUES ('Title 3', 'Content 3');

INSERT INTO comments (content, post_id) VALUES ('Comment 1', 1);
INSERT INTO comments (content, post_id) VALUES ('Comment 2', 1);
INSERT INTO comments (content, post_id) VALUES ('Comment 3', 1);
INSERT INTO comments (content, post_id) VALUES ('Comment 4', 1);
INSERT INTO comments (content, post_id) VALUES ('Comment 5', 2);
INSERT INTO comments (content, post_id) VALUES ('Comment 6', 2);