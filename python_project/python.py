# helloTest.py
# at the end point / call method hello which returns "hello world"
from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello():
  return 'Hello World!'
if _name_ == '_main_':
  app.run(host='0.0.0.0')


import sqlite3
DATABASE_NAME = "moviedb"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def insert_movie(name, rating):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO movie(name, rating) VALUES (?, ?)"
    cursor.execute(statement, [name, rating])
    db.commit()
    return True

def get_movie_by_name(name):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT name, rating FROM movie WHERE name = ?"
    cursor.execute(statement, [name])
    return cursor.fetchone()

In this file add import for db connection:

from db_connection import *

Then add below API for creating movies

@app.route("/movies", methods=["POST"])
def insert_movie():
    movie_details = request.get_json()
    name = movie_details["name"]
    price = movie_details["rating"]
    result = insert_movie(name, rating)
    return result

API: POST {appUrl}/movies
Request Body (JSON):
{
  "name": "SALAAR",
  "rating": 5
}
