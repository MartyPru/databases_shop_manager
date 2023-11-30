DROP SEQUENCE IF EXISTS cinemas_id_seq;
DROP SEQUENCE IF EXISTS movies_id_seq;
DROP TABLE IF EXISTS cinemas CASCADE;
DROP TABLE IF EXISTS movies CASCADE;
DROP TABLE IF EXISTS cinemas_movies CASCADE;

CREATE SEQUENCE IF NOT EXISTS cinemas_id_seq;
CREATE TABLE cinemas (
  id SERIAL PRIMARY KEY,
  name text,
  city date
);

CREATE SEQUENCE IF NOT EXISTS movies_id_seq;
CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title text,
  release_date date
);

CREATE TABLE cinemas_movies (
  cinema_id int,
  movie_id int,
  constraint fk_cinema foreign key(cinema_id) references cinemas(id) on delete cascade,
  constraint fk_movie foreign key(movie_id) references movies(id) on delete cascade,
  PRIMARY KEY (cinema_id, movie_id)
);