import sqlite3

class City_Name:
    def __init__(self,city_name=''):
        self.city_name = city_name

    def add_city(self):
        connection = sqlite3.connect('weather.db')
        cursor = connection.cursor()

        city1 = (self.city_name,)
        insert_query = "INSERT INTO City VALUES (?)"
        cursor.execute(insert_query, city1)
        connection.commit()
        connection.close()

    def check_existing_city(self):
        connection = sqlite3.connect('weather.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM City"
        cursor.execute(select_query)
        res = cursor.fetchall()

        l = []
        for i in res:
            l.append(*i)
        if self.city_name in l:
            connection.close()
            return 'exists'
        else:
            return 'notexists'

    def get_city(self):
        connection = sqlite3.connect('weather.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM City"
        cursor.execute(select_query)
        res = cursor.fetchall()
        connection.close()
        return res

    def delete_city(self):
        connection = sqlite3.connect('weather.db')
        cursor = connection.cursor()

        city = (self.city_name,)
        delete_query = "DELETE FROM City WHERE name = (?)"
        cursor.execute(delete_query,city)
        connection.commit()
        connection.close()





