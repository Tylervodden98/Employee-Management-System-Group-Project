
class Employee:
    dict_user = {}
    languages = []
    favorite_language = []

    def __init__(self, id, first_name, last_name, age, years_coding, birthday, date_of_employment, salary, department):
        self.dict_user["id"] = id
        self.dict_user["first_name"] = first_name
        self.dict_user["last_name"] = last_name
        self.dict_user["age"] = age
        self.dict_user["years_coding"] = years_coding
        self.dict_user["birthday"] = birthday
        self.dict_user["date_of_employment"] = date_of_employment
        self.dict_user["salary"] = salary
        self.dict_user["department"] = department
        

    def print_emp(self):
        for pairs in self.dict_user.items():
            print(f"{pairs[0]} = {pairs[1]}")

    def return_emp(self):
        return self.dict_user

