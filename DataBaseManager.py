import sqlite3
from sqlite3 import Error
from Assignments.FinalProject.Person import Person
from Assignments.FinalProject.Address import Address
from Assignments.FinalProject.Device import Device
from Assignments.FinalProject.Dataplan import DataPlan
from Assignments.FinalProject.ISP import ISP


class Database:
    def __init__(self, date_file):
        self.connection = self.create_connection(date_file)

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as e:
            print("the error {} occurred".format(e))
        return connection

    def execute_query(self, query, params=()):
        cursor = self.connection.cursor()
        # try:
        cursor.execute(query, params)
        self.connection.commit()
        # except Error as e:
        #     print("the error {} occurred".format(e))

    def execute_read_query(self, query, params=()):
        cursor = self.connection.cursor()
        # try:
        cursor.execute(query, params)
        self.connection.commit()
        result = cursor.fetchall()
        return result
        # except Error as e: \
        #         print("the error {} occurred".format(e))


def main():
    db = Database('finalproject.db')
    people = Person(db)
    devices = Device(db)
    dataplans = DataPlan(db)
    addresses = Address(db)
    ISPs = ISP(db)
    people.add_person("Jim", 1234567890, "jim1035@wildcats.unh.edu")
    print(people.view_person("Jim"))
    ISPs.add_ISP(1, 'Verizon', 1)
    addresses.add_address("83 Main St", "Durham", "NH", "03824", "USA", 1, "Jim")
    print(addresses.view_address('Jim'))


if __name__ == "__main__":
    main()
