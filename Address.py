class Address:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS addresses (street TEXT NOT NULL,\
                 city TEXT NOT NULL, state TEXT NOT NULL, " \
                "postal_code TEXT NOT NULL, country TEXT NOT NULL, " \
                "plan_id INTEGER NOT NULL, occupant TEXT NOT NULL," \
                "FOREIGN KEY (plan_id) REFERENCES ISPs(ID), " \
                "FOREIGN KEY (occupant) REFERENCES people(name) ON DELETE CASCADE ) ;"
        self.db.execute_query(query)

    def add_address(self, street, city, state, postal_code, country, plan_id, occupant):
        query = "INSERT INTO addresses (street, city, state, postal_code, country, plan_id, occupant)" \
                "VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = (street, city, state, postal_code, country, plan_id, occupant)
        self.db.execute_query(query, params)

    def view_address(self, occupant):
        query = "SELECT * FROM addresses WHERE occupant = ?"
        params = (occupant,)
        results = self.db.execute_read_query(query, params)
        return results

    def remove_address(self, occupant):
        query = "DELETE FROM addresses WHERE occupant = ?"
        params = (occupant,)
        self.db.execute_query(query, params)
