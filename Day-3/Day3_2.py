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

    query = "select * from empinf;"

    cursor = conn.cursor()

    cursor.execute(query)

    records = cursor.fetchall()

    # for l in records:
    #     for ele in l:
    #         print(ele, end=" ")
    #     print()
    for row in records:
        # print('\t'.join(row))
        print('\t'.join(map(str,row)))

    cursor.close()
    conn.close()

def retrieve_emp_by_dept(dept):
    conn = get_connection()

    query = f"select * from empinf where department = '{dept}';"

    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    # for l in records:
    #     for ele in l:
    #         print(ele, end=" ")
    #     print()
    for row in records:
        # print('\t'.join(row))
        print('\t'.join(map(str,row)))

    cursor.close()
    conn.close()

def retrieve_sal_high_low():
    conn = get_connection()
    ch = int(input("Enter 1 for highest salary and 0 for lowest salary: "))
    print()
    if ch ==1:
        query = "select * from empinf order by salary DESC LIMIT 1;"

    elif ch ==0:
        query = "select * from empinf order by salary ASC LIMIT 1;"

    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    # for l in records:
    #     for ele in l:
    #         print(ele, end=" ")
    #     print()
    for row in records:
        # print('\t'.join(row))
        print('\t'.join(map(str,row)))

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
    print("3. Delete employee")
    print("4. Display all employees")
    print("5. Display employees of certain department")
    print("6. Display employee with highest/lowest salary")
    print()

    choice = int(input("Enter your choice: "))
    print()

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

        case 4:
            retrieve_all_employee()

        case 5:
            dep = input("Enter dept: ")
            print()
            retrieve_emp_by_dept(dep)

        case 6: 
            retrieve_sal_high_low()

        case _:
            print("Invalid Input!!")
    


