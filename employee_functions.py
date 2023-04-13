import csv
import datetime as dt
import os
import random
import json
import employee

# User input functions for employee class

# Name Function

global employee_list

#first and last name functions
def get_fname():
    while True:
        try:
            fname = input("What is your first name?\n>")
            break
        except ValueError:
            print("Please enter a number for your age!\n> ")
        except TypeError:
            print("Please enter a number for your age!\n> ")
            
    
    return fname

def get_lname():
    while True:
        try:
            lname = input("What is your last name?\n>")
            break
        except ValueError:
            print("Please enter a number for your age!\n> ")
        except TypeError:
            print("Please enter a number for your age!\n> ")
            
    return lname

# Age function


def get_age():
    while True:
        try:
            age = int(input("Please enter your age: \n> "))
            break
        except ValueError:
            print("Please enter a number for your age!\n> ")
        except TypeError:
            print("Please enter a number for your age!\n> ")
    return age

# Years Coding Function


def get_years_coding():
    while True:
        try:
            coding = int(
                input("Please enter your amount of years coding: \n> "))
            break
        except ValueError:
            print("Please enter a number for your years of experience coding!\n> ")
        except TypeError:
            print("Please enter a number for your years of experience coding!\n> ")
    return coding

#Birthdeay function
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
            print(f"{e}: Please enter all three inputs as 'YYYY' 'MM' 'DD'\n> ")
    return birthday

#employment date function
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
            print(f"{e}: Please enter all three inputs as 'YYYY' 'MM' 'DD'\n> ")
    return employment_date
#salary function
def get_salary():
    while True:
        try:
            age = int(input("Please enter your salary (rounded to the nearest dollar): \n> "))
            break
        except ValueError:
            print("Please enter a number for your salary!\n> ")
        except TypeError:
            print("Please enter a number for your salary!\n> ")
    return age
#id function
def get_id():
    with open("./employees.json", "r") as json_file:
          
        data = json.load(json_file)
        data = data['emp_details']
         
        ids = [int(val['id']) for val in data]
    
    while True:
        try:
            userid = random.randint(1000,9999)
            if userid in ids:
                raise Exception('User Id exists')
            break
        except:
            pass
    
    return userid
#department function
def get_department():
    return input("Please enter your department: \n> ")
#number of employees function
def get_num_employee():
    while True:
        try:
            num_employee = int(
                input("How many employees you want to add?\n> "))
            break
        except ValueError:
            print("Please enter an integer for how many employees you want:\n> ")
        except TypeError:
            print(
                "Please enter an integer type number for how many employees you want:\n> ")
    return num_employee
#list of employees function
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

#may not even be needed?
def printlist(self, list):
    for employee in list:
        print("ID: " + employee.dict_user["id"])
        print(
            "Name: " + employee.dict_user["first_name"] + " " + employee.dict_user["last_name"])
        print("Age: " + employee.dict_user["age"])
        print("Years Coding: " + employee.dict_user["years_coding"])
        print("Birthday: " + employee.dict_user["birthday"])
        print("Date of Employment: " + str(employee.dict_user["date_of_employment"]))
        print("Salary: $" + str(employee.dict_user["salary"]))
        print("Department: " + employee.dict_user["department"])
        print()


#add employee to dictionary function
def add():
    print("You are adding a new employee\n")
    
    emp = employee.Employee(
        id = get_id(), 
        first_name = get_fname(), 
        last_name = get_lname(), 
        age = get_age(),
        years_coding = get_years_coding(),
        birthday = get_birthday_info(), 
        date_of_employment= get_date_of_employment(), 
        salary = get_salary(), 
        department = get_department())
    
    with open("employees.json", "r") as outfile:
        data = json.load(outfile)
        data = data['emp_details']
    with open("employees.json", "w") as outfile:

        data.append(emp.dict_user)
        newdict = {'emp_details': data}
        json.dump(newdict,outfile, indent=4)
    
    return

#remove employee to dictionary function
def remove_employee():
    while True: 
        try:
            id_to_delete = input("""\nPlease note you will not be able to recover deleted employee. 
                                    For the employee you'd like to delete, please enter their ID: """)

            # read and write to json file
            with open("employees.json", "r") as employee_json_file:
                # the json.load() function which accepts a file object and does the f.read() part for you under the hood
                emp_data = json.load(employee_json_file)
                # use a for loop to iterate through JSON object returned as a dictionary 
                for i, emp_dict in enumerate (emp_data["emp_details"]):
                    # check to see if employee with given id exists
                    print(emp_dict["id"])
                    if id_to_delete == emp_dict["id"]:
                        # remove dictionary containing employee id 
                        emp_data["emp_details"].pop(i)
                        print(emp_data)
                    else:
                        break
                # write changes back to json file 
            with open("employees.json", "w") as employee_json_file:
                json_string = json.dumps(emp_data, indent=4)
                employee_json_file.write(json_string)

        except:    
            print("Sorry this employee doesn't exist. Please enter a valid employee id.")
            # if user wants to go back to main menu ???

            # loop through and collect all ids into a list

