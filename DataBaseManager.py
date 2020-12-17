import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, date_file):
        self.connection = self.create_connection(date_file)

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print("the error {} occurred".format(e))
        return connection

    def execute_query(self, query, params=()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print("the error {} occurred".format(e))

    def execute_read_query(self, query, params=()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            result = cursor.fetchall()
            return result
        except Error as e:
            print("the error {} occurred".format(e))
