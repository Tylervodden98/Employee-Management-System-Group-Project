import csv
import datetime as dt
import os

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

# Years Coding Function


def years_coding():
    while True:
        try:
            coding = int(
                input("Please enter your amount of years coding: "))
            break
        except ValueError:
            print("Please enter a number for your years of experience coding!")
        except TypeError:
            print("Please enter a number for your years of experience coding!")
    return coding


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


def first_languages():
    languages = []
    for num in range(1, 4):
        languages.append(
            input(f"Enter {num} of 3 of your first coding languages: ").capitalize())
    return languages


def favorite_languages():
    favorite_language = []
    for num in range(1, 4):
        favorite_language.append(
            input(f"Enter {num} of 3 of your favorite coding languages: ").capitalize())
    return favorite_language


def print_csv(dict_user: dict):
    # Check if file exists, if it does append to it
    if os.path.isfile(f"./{dict_user['name']}.csv"):
        with open(f"{dict_user['name']}.csv", "a") as employee:
            for key, value in dict_user.items():
                employee.write(f"{key}:{value}\n")
    else:
        # Open file and write to employees.csv if it doesnt exist
        with open(f"{dict_user['name']}.csv", "wt") as employee:
            for key, value in dict_user.items():
                employee.write(f"{key}:{value}\n")


# def employee():

#     dict_user = {}
#     # Ask user for their entries to the dictionary
#     dict_user["name"] = get_name()
#     dict_user["age"] = get_age()
#     dict_user["years coding"] = years_coding()

#     dict_user["birthday"] = birthday_info()
#     # Ask for their first three programming languages as tuple
#     languages = first_languages()
#     tuple_language = tuple(languages)

#     # Ask for their 3 favourite coding languages as list
#     favorite_language = favorite_languages()

#     # Create a set that is an intersection of first 3 languages, and favorite languages
#     language_intersection = list(set(languages) & set(favorite_language))

#     # Add all the collections to the dictionary
#     dict_user["first_languages"] = languages
#     dict_user["favorite_languages"] = favorite_language
#     dict_user["language_intersection"] = language_intersection

#     # Write to csv file
#     print_csv(dict_user)

#     for pairs in dict_user.items():
#         print(f"{pairs[0]} = {pairs[1]}")

#     # Return employee in list
#     return dict_user


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
