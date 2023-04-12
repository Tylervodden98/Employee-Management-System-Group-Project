import csv
import datetime as dt
import os
import employee
import employee_functions as emp
import uuid

def main():

    num_employee = emp.num_employee()

    employee_comp = []
    for _ in range(0, num_employee):

        full_name = emp.get_name().split()
        new_emp = employee.Employee(id = emp.get_id(), #randomly generate UUID
                                    first_name=full_name[0].capitalize(),
                                    last_name=full_name[1].capitalize(),  #error check this later
                                    age=str(emp.get_age()), 
                                    years_coding=str(emp.years_coding()), 
                                    birthday=emp.birthday_info(), 
                                    first_languages=emp.first_languages(), 
                                    favorite_languages=emp.favorite_languages())

        employee_comp.append(new_emp)

    emp.printlist(emp, employee_comp)

main()
