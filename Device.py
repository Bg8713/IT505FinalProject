import csv


class Device:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS devices (plan_id TEXT NOT NULL,\
         name TEXT NOT NULL, type TEXT NOT NULL, owner TEXT NOT NULL, " \
                "FOREIGN KEY (plan_id) REFERENCES dataplans(ID), FOREIGN KEY (owner) REFERENCES person(name));"
        self.db.execute_query(query)

    def add_device(self, plan_id, name, device_type):
        query = "INSERT INTO devices (plan_id, name, type) VALUES (?, ?, ?)"
        params = (plan_id, name, device_type)
        self.db.execute_query(query, params)

    def view_device(self, name):
        query = "SELECT * FROM devices WHERE name = ?"
        params = tuple(name,)
        results = self.db.execute_read_query(query, params)
        return results

    def remove_device(self, name):
        query = "DELETE FROM device WHERE name = ?"
        params = (name,)
        self.db.execute_query(query, params)

    def reset_table(self):
        query = "DROP TABLE devices"
        self.db.execute_query(query)
        query = "CREATE TABLE IF NOT EXISTS devices (plan_id TEXT NOT NULL,\
                 name TEXT NOT NULL, type TEXT NOT NULL, owner TEXT NOT NULL, " \
                "FOREIGN KEY (plan_id) REFERENCES dataplans(ID), FOREIGN KEY (owner) REFERENCES person(name));"
        self.db.execute_query(query)

    def import_devices(self, file):
        filename = 'uploads/' + file
        with open(filename, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                self.add_device(
                    row['plan_id'],
                    row['name'],
                    row['type'],
                    row['owner']
                )
