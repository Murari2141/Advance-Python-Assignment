" 21) Write a Python program to create a database and a table using SQLite3."

import sqlite3

connect = sqlite3.connect('table.db')

cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS USER(id INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER)')

connect.commit()

connect.close()
