import csv


class Address:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        # Creates table

        query = "CREATE TABLE IF NOT EXISTS addresses (street TEXT NOT NULL,\
                 city TEXT NOT NULL, state TEXT NOT NULL, " \
                "postal_code TEXT NOT NULL, country TEXT NOT NULL, " \
                "plan_id INTEGER NOT NULL, occupant TEXT NOT NULL," \
                "FOREIGN KEY (plan_id) REFERENCES ISPs(ID), " \
                "FOREIGN KEY (occupant) REFERENCES people(name) ON DELETE CASCADE ) ;"
        self.db.execute_query(query)

    def add_address(self, street, city, state, postal_code, country, plan_id, occupant):
        # Creates element in table

        query = "INSERT INTO addresses (street, city, state, postal_code, country, plan_id, occupant)" \
                "VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = (street, city, state, postal_code, country, plan_id, occupant)
        self.db.execute_query(query, params)

    def view_address(self, occupant):
        # Views one element from table

        query = "SELECT * FROM addresses WHERE occupant = ?"
        params = (occupant,)
        results = self.db.execute_read_query(query, params)
        return results

    def view_all_addresses(self):
        # Views all elements in the table

        query = "SELECT * FROM addresses"
        results = self.db.execute_read_query(query)
        return results

    def remove_address(self, occupant):
        # Removes an element from the table

        query = "DELETE FROM addresses WHERE occupant = ?"
        params = (occupant,)
        self.db.execute_query(query, params)

    def reset_table(self):
        # Resets the table

        query = "DROP TABLE addresses"
        self.db.execute_query(query)
        query = "CREATE TABLE IF NOT EXISTS addresses (street TEXT NOT NULL,\
                         city TEXT NOT NULL, state TEXT NOT NULL, " \
                "postal_code TEXT NOT NULL, country TEXT NOT NULL, " \
                "plan_id INTEGER NOT NULL, occupant TEXT NOT NULL," \
                "FOREIGN KEY (plan_id) REFERENCES ISPs(ID), " \
                "FOREIGN KEY (occupant) REFERENCES people(name) ON DELETE CASCADE ) ;"
        self.db.execute_query(query)

    def import_addresses(self, file):
        # Imports CSV to table
        # TODO: not currently implemented

        filename = 'uploads/' + file
        with open(filename, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                self.add_address(
                    row['street'],
                    row['city'],
                    row['state'],
                    row['postal_code'],
                    row['country'],
                    row['plan_id'],
                    row['occupant']
                )
