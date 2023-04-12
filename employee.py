
class Employee:
    dict_user = {}
    languages = []
    favorite_language = []

    def __init__(self, id, first_name, last_name, age, years_coding, birthday, first_languages, favorite_languages ):
        self.dict_user["id"] = id
        self.dict_user["first_name"] = first_name
        self.dict_user["last_name"] = last_name
        self.dict_user["age"] = age
        self.dict_user["years_coding"] = years_coding
        self.dict_user["birthday"] = birthday
        self.dict_user["first_languages"] = first_languages
        self.dict_user["favorite_languages"] = favorite_languages
        
    dict_user["language_intersection"] = list(
        set(languages) & set(favorite_language))

    def print_emp(self):
        for pairs in self.dict_user.items():
            print(f"{pairs[0]} = {pairs[1]}")

    def return_emp(self):
        return self.dict_user
