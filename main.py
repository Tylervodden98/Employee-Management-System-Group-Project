import csv
import datetime as dt
import os
import employee
import employee_functions as emp


while True:
    try:
        num_employee = int(input("How many employees you want to add?"))
        break
    except ValueError:
        print("Please enter an integer for how many employees you want:")
    except TypeError:
        print("Please enter an integer type number for how many employees you want:")
print(num_employee)


def main():

    employee_comp = []
    for _ in range(0, num_employee):
        new_emp = employee.Employee(name=emp.get_name(), age=emp.get_age(), years_coding=emp.years_coding(
        ), birthday=emp.birthday_info(), languages=emp.first_languages(), favorite_language=emp.favorite_languages())
        employee_comp.append(new_emp)

    # employee_comp = [E.Employee() for num_person in range(0, number_employee)]

    for e in employee_comp:
        print(e.dict_user)

    print(employee_comp)


main()
