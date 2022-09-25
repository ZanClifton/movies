import os
import datetime
import psycopg2

from dotenv import load_dotenv

load_dotenv()

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT, 
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    users_username TEXT,
    movies_id INTEGER,
    FOREIGN KEY(users_username) REFERENCES users(username),
    FOREIGN KEY(movies_id) REFERENCES movies(id)
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (%s, %s);"

INSERT_USER = "INSERT INTO users (username) VALUES (%s);"

DELETE_MOVIE = "DELETE FROM movies WHERE title = %s;"

SELECT_ALL_MOVIES = "SELECT * FROM movies ORDER BY id;"

SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > %s ORDER BY id;"

SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM movies
JOIN watched ON movies.id = watched.movies_id
JOIN users ON users.username = watched.users_username
WHERE users.username = %s
ORDER BY id;"""

INSERT_WATCHED_MOVIE = "INSERT INTO watched (users_username, movies_id) VALUES (%s, %s);"

SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE %s;"


connection = psycopg2.connect(os.environ["DATABASE_URL"])


def create_table():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHLIST_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))


def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username,))


def delete_movie(title):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_MOVIE, (title,))


def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp, ))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()


def search_movies(query):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES, (f"%{query}%",))
            return cursor.fetchall()


def watch_movie(watcher_name, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIE, (watcher_name, movie_id))


def get_watched_movies(watcher_name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES, (watcher_name,))
            return cursor.fetchall()
