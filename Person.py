import csv


class Person:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS people (name TEXT NOT NULL PRIMARY KEY ,\
         phone_number INTEGER NOT NULL, email_address TEXT NOT NULL );"
        self.db.execute_query(query)

    def add_person(self, name, phone, email):
        query = "INSERT INTO people (name, phone_number, email_address) VALUES (?, ?, ?)"
        params = (name, phone, email)
        self.db.execute_query(query, params)

    def view_person(self, name):
        query = "SELECT * FROM people WHERE name = ?"
        params = (name,)
        results = self.db.execute_read_query(query, params)
        return results

    def remove_person(self, name):
        query = "DELETE FROM people WHERE name = ?"
        params = (name,)
        self.db.execute_query(query, params)

    def reset_table(self):
        query = "DROP TABLE people"
        self.db.execute_query(query)
        query = "CREATE TABLE IF NOT EXISTS people (name TEXT NOT NULL PRIMARY KEY ,\
                 phone_number INTEGER NOT NULL, email_address TEXT NOT NULL );"
        self.db.execute_query(query)

    def import_people(self, file):
        filename = 'uploads/' + file
        with open(filename, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                self.add_person(
                    row['name'],
                    row['phone_number'],
                    row['email_address']
                )
