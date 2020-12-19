import csv


class DataPlan:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        # Creates table

        query = "CREATE TABLE IF NOT EXISTS dataplans (ID TEXT NOT NULL PRIMARY KEY ,\
         name TEXT NOT NULL, data_cap TEXT NOT NULL, cost REAL NOT NULL );"
        self.db.execute_query(query)

    def add_dataplan(self, ID, name, data_cap, cost):
        # Creates element in table

        query = "INSERT INTO dataplans (ID, name, data_cap, cost) VALUES (?, ?, ?, ?)"
        params = (ID, name, data_cap, cost)
        self.db.execute_query(query, params)

    def view_dataplan(self, name):
        # Views one element from table

        query = "SELECT * FROM dataplans WHERE name = ?"
        params = (name,)
        results = self.db.execute_read_query(query, params)
        return results

    def view_all_dataplans(self):
        # Views all elements in the table

        query = "SELECT * FROM dataplans"
        results = self.db.execute_read_query(query)
        return results

    def remove_dataplan(self, name):
        # Removes an element from the table

        query = "DELETE FROM dataplans WHERE name = ?"
        params = (name,)
        self.db.execute_query(query, params)

    def reset_table(self):
        # Resets the table

        query = "DROP TABLE dataplans"
        self.db.execute_query(query)
        query = "CREATE TABLE IF NOT EXISTS dataplans (ID TEXT NOT NULL PRIMARY KEY ,\
                 name TEXT NOT NULL, data_cap TEXT NOT NULL, cost REAL NOT NULL );"
        self.db.execute_query(query)

    def import_dataplans(self, file):
        # Imports CSV to table
        # TODO: not currently implemented

        filename = 'uploads/' + file
        with open(filename, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                self.add_dataplan(
                    row['ID'],
                    row['name'],
                    row['data_cap'],
                    row['cost'],
                )
