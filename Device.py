class Device:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS devices (plan_id TEXT NOT NULL,\
         name TEXT NOT NULL, type TEXT NOT NULL, owner TEXT NOT NULL );"
        self.db.execute_query(query)

    def add_device(self, plan_id, name, device_type):
        query = "INSERT INTO devices (plan_id, name, type) VALUES (?, ?, ?)"
        params = (plan_id, name, device_type)
        self.db.execute_query(query, params)

    def view_device(self, name):
        query = "SELECT * FROM devices WHERE name = ?"
        params = tuple(name)
        results = self.db.execute_read_query(query, params)
        return results
