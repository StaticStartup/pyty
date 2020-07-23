from sqlite_ import sqlite

db = sqlite('data/test.db')
db.createFromSQL('CREATE TABLE IF NOT EXISTS projects (id integer PRIMARY KEY, name text NOT NULL, begin_date text, end_date text);')