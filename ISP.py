class ISP:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS ISP (ID TEXT NOT NULL,\
         internet_plan TEXT NOT NULL, modem_provided INTEGER NOT NULL );"
        self.db.execute_query(query)

    def add_ISP(self, ID, internet_plan, modem_provided):
        query = "INSERT INTO ISP (ID, internet_plan, modem_provided) VALUES (?, ?, ?)"
        params = (ID, internet_plan, modem_provided)
        self.db.execute_query(query, params)

    def view_device(self, occupant):
        query = "SELECT * FROM addresses WHERE occupant = ?"
        params = tuple(occupant)
        results = self.db.execute_read_query(query, params)
        return results
