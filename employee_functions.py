import csv
import datetime as dt
import os
import random

# User input functions for employee class

# Name Function


def get_name():
    return input("Please enter your name: ").capitalize()

# Age function


def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Please enter a number for your age!")
        except TypeError:
            print("Please enter a number for your age!")
    return age

# Birthday Function


def birthday_info():
    while True:
        try:
            birthday_info = input(
                "Please enter your birthday in 'YYYY' 'MM' 'DD' seperated by spaces: ")
            birthday_dates = birthday_info.split(" ")
            # Check bday dates
            birthday = dt.datetime(
                year=int(birthday_dates[0]), month=int(birthday_dates[1]), day=int(birthday_dates[2]))
            break
        except ValueError as e:
            print(f"{e}")
        except IndexError as e:
            print(f"{e}: Please enter all three inputs as 'YYYY' 'MM' 'DD'")
    return birthday


def num_employee():
    while True:
        try:
            num_employee = int(input("How many employees you want to add?"))
            break
        except ValueError:
            print("Please enter an integer for how many employees you want:")
        except TypeError:
            print("Please enter an integer type number for how many employees you want:")
    return num_employee
