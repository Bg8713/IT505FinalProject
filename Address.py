class Address:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS addresses (street TEXT NOT NULL,\
                 city TEXT NOT NULL, state TEXT NOT NULL, " \
                "postal_code INTEGER NOT NULL, country TEXT NOT NULL, " \
                "plan_ID INTEGER NOT NULL, occupant TEXT NOT NULL );"
        self.db.execute_query(query)

    def add_address(self, street, city, state, postal_code, country, plan_id):
        query = "INSERT INTO addresses (street, city, state, postal_code, country, plan_id)" \
                "VALUES (?, ?, ?, ?, ?, ?)"
        params = (street, city, state, postal_code, country, plan_id)
        self.db.execute_query(query, params)

    def view_device(self, occupant):
        query = "SELECT * FROM addresses WHERE occupant = ?"
        params = tuple(occupant)
        results = self.db.execute_read_query(query, params)
        return results
