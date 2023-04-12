import csv
import datetime as dt
import os
import employee
import employee_functions as emp


def menu():
    # Ask user for what they would like to do
    while True:
        try:
            choice = input(
                "Please enter 'L' for Listing Employees, 'A' for Adding Employees, 'U' for Updating Employees, 'R' for Removing Employees, 'Q' to exit app: \n> ").upper()
            if choice == 'L':
        # Call Employee Updating Function
                emp.list_employees()
                pass
            elif choice == 'Q':
        # Exit Application
                quit()
            elif choice == 'R':
        # Call Employee Removing Function
                pass
            elif choice == 'A':
        # Call Employee Adding Function
                pass
            elif choice == 'U':
        # Call Employee Updating Function
                pass
            else:
                raise MenuInputException()
        except MenuInputException:
            print("Please enter a valid input 'L' 'A' 'U' 'R' 'Q'")

class MenuInputException(Exception):
    pass


def main():

    menu()

    # Adding Employee move this to employee_function when done
    # employee_comp = []
    # for _ in range(0, num_employee):
    #     new_emp = employee.Employee(name=emp.get_name(), age=emp.get_age(), years_coding=emp.years_coding(
    #     ), birthday=emp.birthday_info(), languages=emp.first_languages(), favorite_language=emp.favorite_languages())
    #     employee_comp.append(new_emp)

    # # employee_comp = [E.Employee() for num_person in range(0, number_employee)]
    # for e in employee_comp:
    #     print(e.dict_user)

    # print(employee_comp)


main()
