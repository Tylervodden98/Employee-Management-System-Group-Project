while True:
    try:
        num_employee = int(input("How many employees you want to add?"))
        break
    except ValueError:
        print("Please enter an integer for how many employees you want:")
    except TypeError:
        print("Please enter an integer type number for how many employees you want:")
print(num_employee)