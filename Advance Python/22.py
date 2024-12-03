"22) Write a Python program to insert data into an SQLite3 database and fetch it."
import sqlite3

connect = sqlite3.connect('table.db')

cursor = connect.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS USER(id INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER)')
cursor.execute('INSERT INTO USER(NAME, AGE) VALUES ("ajay", 25)')

connect.commit()

connect.close()
