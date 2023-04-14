
class Employee:
    dict_user = {}

    def __init__(self, id: str, first_name: str, last_name: str, age: int, years_coding: int, birthday: str, date_of_employment: str, salary: int, department: str):
        self.dict_user["id"] = id
        self.dict_user["first_name"] = first_name
        self.dict_user["last_name"] = last_name
        self.dict_user["age"] = age
        self.dict_user["years_coding"] = years_coding
        self.dict_user["date_of_employment"] = date_of_employment
        self.dict_user["salary"] = salary
        self.dict_user["birthday"] = birthday
        self.dict_user["department"] = department
