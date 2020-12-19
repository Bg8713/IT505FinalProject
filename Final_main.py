from flask import Flask, request
from flask import render_template, redirect, url_for

from Person import Person
from Address import Address
from Device import Device
from Dataplan import DataPlan
from ISP import ISP

from DataBaseManager import Database

app = Flask(__name__)


def dbconn():
    # instantiate a connection to the database
    conn = Database('finalproject.db')

    return conn


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/people", methods=['GET', 'POST'])
def ModifyPeople():
    # instance of connection to the database
    conn = dbconn()

    # retrieve all the people in the people Table
    # people = conn.execute_read_query("SELECT * FROM people")

    if request.method == 'POST':
        person_name = request.form['name']
        person_phone = request.form['phone']
        person_email = request.form['email']

        person_obj = Person(conn)  # person object

        person_obj.add_person(person_name, person_phone, person_email)

        # person = person_obj.view_person(person_name)
        # retrieve plus the added people
        # people = conn.execute_read_query("SELECT * FROM people")

        return redirect('/people/list')
    else:
        return render_template('person.html')


@app.route('/people/list')
def people_list():
    conn = dbconn()
    rows = conn.execute_read_query("SELECT * FROM people")
    return render_template('person.view.html', people=rows)


@app.route("/deletePerson/<string:name>")
def deletePerson(name):
    conn = dbconn()
    person_obj = Person(conn)
    person_obj.remove_person(name)

    return redirect('/people/list')


@app.route("/addresses", methods=['GET', 'POST'])
def ModifyAddresses():
    conn = dbconn()

    # retrieve all addresses
    # addresses = conn.execute_read_query("SELECT * FROM addresses")
    # address = addresses[0]

    # retrieve isp plan and occupant
    # isp = conn.execute_read_query("SELECT * FROM ISPs")[0][0]
    # occupant = conn.execute_read_query("SELECT * FROM people")[0][0]

    if request.method == 'POST':
        address_street = request.form['street']
        address_city = request.form['city']
        address_state = request.form['state']
        address_postal_code = request.form['postal_code']
        address_country = request.form['country']

        isp = request.form['plan_id']  # hidden ISP Plan
        occupant = request.form['Occupant']

        address = Address(conn)  # Address object
        address.add_address(address_street, address_city, address_state, address_postal_code, address_country, isp,
                            occupant)

        # addresses = conn.execute_read_query("SELECT * FROM addresses")

        return redirect("/addresses/list")

    return render_template('address.html')


@app.route('/addresses/list')
def addresses_list():
    conn = dbconn()
    rows = conn.execute_read_query("SELECT * FROM addresses")
    return render_template('address.view.html', addresses=rows)


@app.route("/deleteAddress/<string:name>")
def deleteAddress(name):
    conn = dbconn()
    address_obj = Address(conn)
    address_obj.remove_address(name)

    return redirect('/addresses/list')


@app.route("/devices", methods=['GET', 'POST'])
def ModifyDevices():
    conn = dbconn()
    device_obj = Device(conn)

    # retrieve all devices
    # devices = conn.execute_read_query("SELECT * FROM devices")

    if request.method == 'POST':
        device_plan_id = request.form['plan_id']
        device_name = request.form['name']
        device_type = request.form['type']
        device_owner = request.form['owner']

        device_obj.add_device(device_plan_id, device_name, device_type, device_owner)

        # device = device_obj.view_device(device_name)

        # devices = conn.execute_read_query("SELECT * FROM devices")

        return redirect('/devices/list')

    else:

        return render_template('device.html')


@app.route('/devices/list')
def devices_list():
    conn = dbconn()
    rows = conn.execute_read_query("SELECT * FROM devices")
    dict_list = []
    for row in rows:
        temp = {
            'plan_id': row[0],
            'name': row[1],
            'type': row[2],
            'owner': row[3]
        }
        dict_list.append(temp)
    return render_template('device.view.html', devices=dict_list)


@app.route("/deleteDevice/<string:name>")
def deleteDevice(name):
    conn = dbconn()
    device_obj = Device(conn)
    device_obj.remove_device(name)

    return redirect('/devices/list')


@app.route("/data-plans", methods=['GET', 'POST'])
def ModifyDataPlans():
    conn = dbconn()

    # all data plans
    # dataplans = conn.execute_read_query("SELECT * FROM dataplans")

    if request.method == 'POST':
        dataplan_id = request.form['ID']
        dataplan_name = request.form['name']
        dataplan_data_cap = request.form['data_cap']
        dataplan_cost = request.form['cost']

        dataplan_obj = DataPlan(conn)
        dataplan_obj.add_dataplan(dataplan_id, dataplan_name, dataplan_data_cap, dataplan_cost)

        # data = dataplan_obj.view_dataplan(dataplan_name)

        # dataplans = conn.execute_read_query("SELECT * FROM dataplans")

        return redirect('/dataplans/list')

    else:
        return render_template('data.html')


@app.route('/dataplans/list')
def dataplans_list():
    conn = dbconn()
    rows = conn.execute_read_query("SELECT * FROM dataplans")
    dict_list = []
    for row in rows:
        temp = {
            'ID': row[0],
            'name': row[1],
            'data_cap': row[2],
            'cost': row[3]
        }
        dict_list.append(temp)
    print(dict_list)
    return render_template('data.view.html', dataplans=dict_list)


@app.route("/deleteDataplan/<string:name>")
def deleteDataplan(name):
    conn = dbconn()
    dataplan_obj = DataPlan(conn)
    dataplan_obj.remove_dataplan(name)

    return redirect('/dataplans/list')


@app.route("/internet-services", methods=['GET', 'POST'])
def ModifyInternetServices():
    conn = dbconn()

    # all isp
    # isps = conn.execute_read_query("SELECT * FROM ISPs")

    # occupant = conn.execute_read_query("SELECT * FROM people")[0][0]

    if request.method == 'POST':
        isp_id = request.form['ID']
        isp_internet_plan = request.form['internet_plan']
        isp_modem_provided = request.form['modem_provided']

        isp_obj = ISP(conn)
        isp_obj.add_ISP(isp_id, isp_internet_plan, isp_modem_provided)

        # isp = isp_obj.view_ISP(occupant)

        return redirect('/ISPs/list')

    else:
        return render_template('internet.html')


@app.route('/ISPs/list')
def ISPs_list():
    conn = dbconn()
    rows = conn.execute_read_query("SELECT * FROM ISPs")
    dict_list = []
    for row in rows:
        temp = {
            'ID': row[0],
            'internet_plan': row[1],
            'modem_provided': row[2]
        }
        dict_list.append(temp)
    return render_template('internet.view.html', ISPs=dict_list)


@app.route("/deleteISP/<string:name>")
def deleteISP(name):
    conn = dbconn()
    ISP_obj = ISP(conn)
    ISP_obj.remove_ISP(name)

    return redirect('/ISPs/list')


@app.route("/load-data-from-csv")
def LoadData():
    return render_template('import.html')


@app.route("/reset")
def ResetDataBase():
    # instantiate the connection object
    conn = dbconn()
    # reset all tables in the database
    person_obj = Person(conn)
    person_obj.reset_table()
    address_obj = Address(conn)
    address_obj.reset_table()
    dataplan_obj = DataPlan(conn)
    dataplan_obj.reset_table()
    isp_obj = ISP(conn)
    isp_obj.reset_table()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
