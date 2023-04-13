import csv
import datetime as dt
import os
import random
import json

# User input functions for employee class

# Name Function

global employee_list


def get_name():
    string = input("Please enter your full name: \n> ")
    while (" " not in string):
        string = input("Please enter your first and last name: \n> ")
    return string

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

def get_department():
    return input("Please enter your department: \n> ")

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
         # check to see if file contains any employees
            with open("employees.json", "r") as employee_json_file:
                emp_data = json.load(employee_json_file)
            if(emp_data["emp_details"] == []):
                print("\nSorry the file is empty. There are no more employees to delete.")
                break
            else:
                id_to_delete = input("\nPlease note you will not be able to recover deleted employee. For the employee you'd like to delete, please enter their ID: ")
                # if employee id of interest is in list of all valid id's
                if id_to_delete in list_of_user_ids:
                    # read and write to json file
                    with open("employees.json", "r") as employee_json_file:
                        emp_data = json.load(employee_json_file)
                        # use a for loop to iterate through JSON object returned as a dictionary 
                        for i, emp_dict in enumerate (emp_data["emp_details"]):
                            # check to see if employee with given id exists
                            if id_to_delete == emp_dict["id"]:
                                # remove dictionary containing employee id 
                                emp_data["emp_details"].pop(i)
                                print(f"\n The employee {emp_dict['first_name']} {emp_dict['last_name']} with employee ID {id_to_delete} was successfully deleted.")

                        # write changes back to json file 
                    with open("employees.json", "w") as employee_json_file:
                        json_string = json.dumps(emp_data, indent=4)
                        employee_json_file.write(json_string)
                    
                else: raise Exception
                break
        except Exception:
            print("\nSorry this is not a valid employee id. Please try again.")   



    


