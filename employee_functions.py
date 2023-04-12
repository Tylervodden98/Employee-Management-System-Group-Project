import csv
import datetime as dt
import os
import random


# User input functions for employee class

# Name Function

global employee_list

def get_name():
    string = input("Please enter your full name: \n> ")
    while(" " not in string):
        string = input("Please enter your first and last name: \n> ")
    return  string

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


def first_languages():
    languages = []
    for num in range(1, 4):
        languages.append(
            input(f"Enter {num} of 3 of your first coding languages: \n> ").capitalize())
    return languages


def favorite_languages():
    favorite_language = []
    for num in range(1, 4):
        favorite_language.append(
            input(f"Enter {num} of 3 of your favorite coding languages: \n> ").capitalize())
    return favorite_language

def get_id():
    pass

def list(list):

    try:
        file = open("employees.json", "r")
        print(file.read())

    except:
        print("Import file does not exist.\n")

def num_employee():
    while True:
        try:
            num_employee = int(input("How many employees you want to add?\n> "))
            break
        except ValueError:
            print("Please enter an integer for how many employees you want:\n> ")
        except TypeError:
            print("Please enter an integer type number for how many employees you want:\n> ")
    return num_employee

def printlist(self, list):
        for employee in list:
            print("ID: " + employee.dict_user["id"])
            print("Name: " + employee.dict_user["first_name"] + " " + employee.dict_user["last_name"])
            print("Age: " + employee.dict_user["age"])
            print("Years Coding: " + employee.dict_user["years_coding"])
            print("Birthday: " + employee.dict_user["birthday"])
            print("First Languages: " + employee.dict_user["first_languages"][0] + ", " +
                  employee.dict_user["first_languages"][1] + ", " +
                   employee.dict_user["first_languages"][2])
            print("Favorite Languages: " + employee.dict_user["favorite_languages"][0] + ", " +
                  employee.dict_user["favorite_languages"][1] + ", " +
                   employee.dict_user["favorite_languages"][2] )
            print()