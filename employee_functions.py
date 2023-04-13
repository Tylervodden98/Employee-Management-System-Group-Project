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


def years_coding():
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


def birthday_info():
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


def num_employee():
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


def printlist(self, list):
    for employee in list:
        print("ID: " + employee.dict_user["id"])
        print(
            "Name: " + employee.dict_user["first_name"] + " " + employee.dict_user["last_name"])
        print("Age: " + employee.dict_user["age"])
        print("Years Coding: " + employee.dict_user["years_coding"])
        print("Birthday: " + employee.dict_user["birthday"])
        print("First Languages: " + employee.dict_user["first_languages"][0] + ", " +
              employee.dict_user["first_languages"][1] + ", " +
              employee.dict_user["first_languages"][2])
        print("Favorite Languages: " + employee.dict_user["favorite_languages"][0] + ", " +
              employee.dict_user["favorite_languages"][1] + ", " +
              employee.dict_user["favorite_languages"][2])
        print()

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

