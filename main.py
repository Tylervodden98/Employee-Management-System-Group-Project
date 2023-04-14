import datetime as dt
import employee_functions as emp


def menu():
    # Ask user for what they would like to do
    while True:
        try:
            choice = input(
                "Please enter 'L' for Listing Employees, 'A' for Adding Employees, 'U' for Updating Employees, 'R' for Removing Employees, 'Q' to exit app: \n> ").upper()
            if choice == 'L':
                # Call Employee Listing Function
                emp.list_employees()
                pass
            elif choice == 'Q':
                # Exit Application
                quit()
            elif choice == 'R':
                # Call Employee Removing Function
                emp.remove_employee()
            elif choice == 'A':
                emp.add_employee()
                pass
            elif choice == 'U':
                # Call Employee Updating Function
                emp.update_employee()
                pass
            else:
                raise MenuInputException()
        except MenuInputException:
            pass


class MenuInputException(Exception):
    def __init__(self):
        print("Please enter a valid input: 'L' 'A' 'U' 'R' 'Q'")


def main():
    menu()


main()
