import sqlite3

connection = sqlite3.connect('weather.db')
cursor = connection.cursor()

create_table = "CREATE TABLE City (name text)"
cursor.execute(create_table)

connection.commit()
connection.close()

