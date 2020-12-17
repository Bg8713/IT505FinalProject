class DataPlan:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS dataplan (ID TEXT NOT NULL,\
         name TEXT NOT NULL, data_cap TEXT NOT NULL, cost REAL NOT NULL );"
        self.db.execute_query(query)

    def add_dataplan(self, ID, name, data_cap, cost):
        query = "INSERT INTO dataplan (ID, name, data_cap, cost) VALUES (?, ?, ?, ?)"
        params = (ID, name, data_cap, cost)
        self.db.execute_query(query, params)

    def view_device(self, name):
        query = "SELECT * FROM dataplan WHERE name = ?"
        params = tuple(name)
        results = self.db.execute_read_query(query, params)
        return results
