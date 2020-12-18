class DataPlan:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS dataplans (ID TEXT NOT NULL PRIMARY KEY ,\
         name TEXT NOT NULL, data_cap TEXT NOT NULL, cost REAL NOT NULL );"
        self.db.execute_query(query)

    def add_dataplan(self, ID, name, data_cap, cost):
        query = "INSERT INTO dataplans (ID, name, data_cap, cost) VALUES (?, ?, ?, ?)"
        params = (ID, name, data_cap, cost)
        self.db.execute_query(query, params)

    def view_dataplan(self, name):
        query = "SELECT * FROM dataplans WHERE name = ?"
        params = (name,)
        results = self.db.execute_read_query(query, params)
        return results

    def remove_dataplan(self, name):
        query = "DELETE FROM dataplans WHERE name = ?"
        params = (name,)
        self.db.execute_query(query, params)
