import employee
import datetime as dt
import random
import json
import employee

# User input functions for employee class

# first and last name functions
def get_fname():
    while True:
        try:
            fname = input("What is your first name?\n>")
            break
        except ValueError:
            print("Please enter a number for your age!")
        except TypeError:
            print("Please enter a number for your age!")

    return fname

def get_lname():
    while True:
        try:
            lname = input("What is your last name?\n>")
            break
        except ValueError:
            print("Please enter a number for your age!")
        except TypeError:
            print("Please enter a number for your age!")

    return lname

# Age function
def get_age():
    while True:
        try:
            age = int(input("Please enter your age: \n> "))
            break
        except ValueError:
            print("Please enter a number for your age!")
        except TypeError:
            print("Please enter a number for your age!")
    return age

# Years Coding Function
def get_years_coding():
    while True:
        try:
            coding = int(
                input("Please enter your amount of years coding: \n> "))
            break
        except ValueError:
            print("Please enter a number for your years of experience coding!")
        except TypeError:
            print("Please enter a number for your years of experience coding!")
    return coding

# Birthdeay function
def get_birthday_info():
    while True:
        try:
            birthday_info = input(
                "Please enter your birthday in 'YYYY' 'MM' 'DD' seperated by spaces: \n> ")
            birthday_dates = birthday_info.split(" ")
            # Check bday dates
            birthday = str(dt.datetime(
                year=int(birthday_dates[0]), month=int(birthday_dates[1]), day=int(birthday_dates[2]))).split()[0]
            break
        except ValueError as e:
            print(f"{e}")
        except IndexError as e:
            print(f"{e}: Please enter all three inputs as 'YYYY' 'MM' 'DD'.")
    return birthday

# employment date function
def get_date_of_employment():
    while True:
        try:
            emp_date = input(
                "Please enter your employment start date in 'YYYY' 'MM' 'DD' seperated by spaces: \n> ")
            emp_dates = emp_date.split(" ")
            # Check employment dates
            employment_date = str(dt.datetime(
                year=int(emp_dates[0]), month=int(emp_dates[1]), day=int(emp_dates[2]))).split()[0]
            break
        except ValueError as e:
            print(f"{e}")
        except IndexError as e:
            print(f"{e}: Please enter all three inputs as 'YYYY' 'MM' 'DD'.")
    return employment_date

# salary function
def get_salary():
    while True:
        try:
            age = int(
                input("Please enter your salary (rounded to the nearest dollar): \n> "))
            break
        except ValueError:
            print("Please enter a number for your salary!")
        except TypeError:
            print("Please enter a number for your salary!")
    return age

# id function
def get_id():
    with open("./employees.json", "r") as json_file:

        data = json.load(json_file)
        data = data['emp_details']

        ids = [int(val['id']) for val in data]

    while True:
        try:
            userid = random.randint(1000, 9999)
            if userid in ids:
                raise Exception('User Id exists.')
            break
        except:
            pass

    return str(userid)

# department function
def get_department():
    departments = ['CEO','COO', 'finance', 'office manager', 'receptionist','dog food taster']

    while True:
        try:
            x = input("Please enter your department: \n> ")
            if x in departments:
                break
            else:
                print("Department does not exist, select another department.")
        except:
            pass
    return x

#number of employees function
def get_num_employee():
    while True:
        try:
            num_employee = int(
                input("How many employees you want to add?\n> "))
            break
        except ValueError:
            print("Please enter an integer for how many employees you want.")
        except TypeError:
            print(
                "Please enter an integer type number for how many employees you want.")
    return num_employee

# list of employees function
def list_employees():

    try:
        file = open("employees.json", "r")
    except:
        print("Import file does not exist.\n")

    emp_list = json.load(file)

    for i in emp_list["emp_details"]:
        print("ID: " + i["id"])
        print("Full Name: " + i["first_name"] + " " + i["last_name"])
        print("Age: " + str(i["age"]))
        print("Department: " + i["department"])
        print("Date of Employment: : " + str(i["date_of_employment"]))
        print("Salary: " + str(i["salary"]))
        print("Birthday: " + str(i["birthday"]))
        print()

# prints out an employee's information neatly and user-friendly
def printlist(employee_entry):
    print("ID: " + employee_entry["id"])
    print("Name: " + employee_entry["first_name"] + " " + employee_entry["last_name"])
    print("Age: " + str(employee_entry["age"]))
    print("Years Coding: " + str(employee_entry["years_coding"]))
    print("Birthday: " + employee_entry["birthday"])
    print("Date of Employment: " + str(employee_entry["date_of_employment"]))
    print("Salary: $" + str(employee_entry["salary"]))
    print("Department: " + employee_entry["department"])
    print()

# add employee to dictionary function
def add_employee():
    print("You are adding a new employee.\n")

    emp = employee.Employee(
        id=get_id(),
        first_name=get_fname(),
        last_name=get_lname(),
        age=get_age(),
        years_coding=get_years_coding(),
        birthday=get_birthday_info(),
        date_of_employment=get_date_of_employment(),
        salary=get_salary(),
        department=get_department())

    with open("employees.json", "r") as outfile:
        data = json.load(outfile)
        data = data['emp_details']
    with open("employees.json", "w") as outfile:

        data.append(emp.dict_user)
        newdict = {'emp_details': data}
        json.dump(newdict, outfile, indent=4)
        print(
            f"Added employee {emp.dict_user['first_name']} {emp.dict_user['last_name']}.")

    return

# remove employee to dictionary function
def remove_employee():
    # create an empty list to store all employee id's
    list_of_user_ids = []
    with open("employees.json", "r") as json_file:
        data = json.load(json_file)
    # append employee id's to list
    for id_dict in data['emp_details']:
        list_of_user_ids.append(id_dict["id"])

    while True:
        try:
         # check to see if file is empty
            with open("employees.json", "r") as employee_json_file:
                emp_data = json.load(employee_json_file)
            if (emp_data["emp_details"] == []):
                print(
                    "\nSorry, the file is empty. There are no more employees to delete.")
                break
            else:
                id_to_delete = input(
                    "\nPlease note you will not be able to recover deleted employee. For the employee you'd like to delete, please enter their ID: \n> ")
                # if employee id of interest is in list of all valid id's
                if id_to_delete in list_of_user_ids:
                    with open("employees.json", "r") as employee_json_file:
                        emp_data = json.load(employee_json_file)
                        # use a for loop to iterate through JSON object returned as a dictionary
                        for i, emp_dict in enumerate(emp_data["emp_details"]):
                            # check to see if employee with given id exists
                            if id_to_delete == emp_dict["id"]:
                                # remove dictionary containing employee id
                                emp_data["emp_details"].pop(i)
                                print(
                                    f"\n The employee {emp_dict['first_name']} {emp_dict['last_name']} with employee ID {id_to_delete} was successfully deleted.")

                    # write changes back to json file
                    with open("employees.json", "w") as employee_json_file:
                        json_string = json.dumps(emp_data, indent=4)
                        employee_json_file.write(json_string)

                else:
                    raise Exception
                break
        except Exception:
            print("\nSorry this is not a valid employee id. Please try again.")

#method to update employee information
def update_employee():
    emp_id = input("Enter employee ID: \n> ")
    # Check if employee with the given ID exists
    with open("./employees.json", "r") as json_file:
        data = json.load(json_file)
        emp_there = False
    for i, emp_dict in enumerate(data['emp_details']):
        # check user id put the user inputted id for "id"
        if emp_id == emp_dict["id"]:
            index = i
            emp_there = True
            pass
    if emp_there:
        print("Employee with ID", emp_id, "found.")
        # keeps track of dictionary keys
        keys = list(data['emp_details'][0].keys())
        try:
            attribute = input(f"Enter attribute to update: {keys} \n> ")
            if attribute in keys and attribute != "id":
                # value = input("Enter new value for attribute: ")
                if attribute == "first_name":
                    value = get_fname()
                    data['emp_details'][index][attribute] = value
                elif attribute == "last_name":
                    value = get_lname()
                    data['emp_details'][index][attribute] = value
                elif attribute == "age":
                    value = get_age()
                    data['emp_details'][index][attribute] = value
                elif attribute == "department":
                    value = get_department()
                    data['emp_details'][index][attribute] = value
                elif attribute == "date_of_employment":
                    value = get_date_of_employment()
                    data['emp_details'][index][attribute] = value
                elif attribute == "salary":
                    value = get_salary()
                    data['emp_details'][index][attribute] = value
                elif attribute == "birthday":
                    value = get_birthday_info()
                    data['emp_details'][index][attribute] = value
            else:
                raise Exception

        except:
            print("Attribute doesnt exist in dictionary.")

        # Update attribute
        print("Employee listing to write: \n")
        printlist( data['emp_details'][index])

    else:
        print("Employee with ID", emp_id, "does not exist.")

    # Write updated employee data to JSON file
    with open('employees.json', 'w') as f:
        json.dump(data, f,indent=4)
