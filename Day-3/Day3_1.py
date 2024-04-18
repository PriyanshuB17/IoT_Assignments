import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"

    )

def create_employee():
    conn = get_connection()

    empid = int(input("Enter empid: "))
    name = input("Enter name: ")
    dept = input("Enter department: ")
    email = input("Enter email: ")
    salary = input("Enter salary: ")
    doj = input("Enter date of joining (dd/mm/yyyy): ")
    
    query = f"insert into empinf values ({empid}, '{name}', '{dept}', '{email}', '{salary}', '{doj}');"
    
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Records added successfully!!")
    cursor.close()
    conn.close()

def update_employee(empid, salary):
    conn = get_connection()

    query = f"update empinf SET salary = %s where empid = %s;"
    val = (salary, empid)

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    print("Record updated successfully!!")

    cursor.close()
    conn.close()

def retrieve_all_employee():
    conn = get_connection()

    query = "select * from empif;"

    cursor = conn.cursor()

    cursor.execute(query)

    records = cursor.fetchall()

    print(records)

    cursor.close()
    conn.close()

def delete_employee(empid):
    conn = get_connection()

    query = f"delete from empinf where empid = %s;"
    val = (empid, )

    cursor = conn.cursor()

    cursor.execute(query, val)

    conn.commit()

    print("Record Deleted!!")

    cursor.close()
    conn.close()

while True:
    print()
    print("Menu:")
    print("0. Exit")
    print("1. Add Employee")
    print("2. Update employee salary")
    print("3. Delete employee details")
    print()

    choice = int(input("Enter your choice: "))

    match choice:
        case 0:
            break

        case 1:
            create_employee()
        
        case 2:
            epid = int(input("Enter employee id: "))
            sal = input("Enter salary: ")
            update_employee(epid, sal)

        case 3:
            epid = int(input("Enter employee id of the employee to be deleted: "))
            delete_employee(epid)

        case default:
            print("Invalid Input!!")
    


