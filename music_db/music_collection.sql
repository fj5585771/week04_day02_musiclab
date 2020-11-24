DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR (255),
    year INT,
    duration VARCHAR(255),
    artist_id INT REFERENCES artists (id),
    genre VARCHAR(255)
);
