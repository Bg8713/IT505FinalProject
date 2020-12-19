import csv


class ISP:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        # Creates table

        query = "CREATE TABLE IF NOT EXISTS ISPs (ID INTEGER NOT NULL PRIMARY KEY ,\
         internet_plan TEXT NOT NULL, modem_provided INTEGER NOT NULL );"
        self.db.execute_query(query)

    def add_ISP(self, ID, internet_plan, modem_provided):
        # Creates element in table

        query = "INSERT INTO ISPs (ID, internet_plan, modem_provided) VALUES (?, ?, ?)"
        params = (ID, internet_plan, modem_provided)
        self.db.execute_query(query, params)

    def view_ISP(self, occupant):
        # Views one element from table

        query = "SELECT * FROM ISPs WHERE occupant = ?"
        params = (occupant,)
        results = self.db.execute_read_query(query, params)
        return results

    def view_all_ISPs(self):
        # Views all elements in the table

        query = "SELECT * FROM ISPs"
        results = self.db.execute_read_query(query)
        return results

    def remove_ISP(self, ID):
        # Removes an element from the table

        query = "DELETE FROM ISPs WHERE ID = ?"
        params = (ID,)
        self.db.execute_query(query, params)

    def reset_table(self):
        # Resets the table

        query = "DROP TABLE ISPs"
        self.db.execute_query(query)
        query = "CREATE TABLE IF NOT EXISTS ISPs (ID INTEGER NOT NULL PRIMARY KEY ,\
                 internet_plan TEXT NOT NULL, modem_provided INTEGER NOT NULL );"
        self.db.execute_query(query)

    def import_ISPs(self, file):
        # Imports CSV to table
        # TODO: not currently implemented

        filename = 'uploads/' + file
        with open(filename, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                self.add_ISP(
                    row['ID'],
                    row['internet_plan'],
                    row['modem_provided'],
                )
