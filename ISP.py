class ISP:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS ISPs (ID INTEGER NOT NULL PRIMARY KEY ,\
         internet_plan TEXT NOT NULL, modem_provided INTEGER NOT NULL );"
        self.db.execute_query(query)

    def add_ISP(self, ID, internet_plan, modem_provided):
        query = "INSERT INTO ISPs (ID, internet_plan, modem_provided) VALUES (?, ?, ?)"
        params = (ID, internet_plan, modem_provided)
        self.db.execute_query(query, params)

    def view_ISP(self, occupant):
        query = "SELECT * FROM ISPs WHERE occupant = ?"
        params = (occupant,)
        results = self.db.execute_read_query(query, params)
        return results

    def remove_ISP(self, name):
        query = "DELETE FROM ISPs WHERE name = ?"
        params = (name,)
        self.db.execute_query(query, params)

    def reset_table(self):
        query = "DROP TABLE ISPs"
        self.db.execute_query(query)
        query = "CREATE TABLE IF NOT EXISTS ISPs (ID INTEGER NOT NULL PRIMARY KEY ,\
                 internet_plan TEXT NOT NULL, modem_provided INTEGER NOT NULL );"
        self.db.execute_query(query)
