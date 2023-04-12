
class Employee:
    dict_user = {}
    languages = []
    favorite_language = []

    def __init__(self, name, age, years_coding, birthday, languages, favorite_language):
        self.dict_user["name"] = name
        self.dict_user["age"] = age
        self.dict_user["years coding"] = years_coding
        self.dict_user["birthday"] = birthday
        self.dict_user["languages"] = languages
        self.dict_user["favorite_languages"] = favorite_language
        self.languages = languages
        self.favorite_language = favorite_language

    dict_user["language_intersection"] = list(
        set(languages) & set(favorite_language))

    def print_emp(self):
        for pairs in self.dict_user.items():
            print(f"{pairs[0]} = {pairs[1]}")

    def return_emp(self):
        return self.dict_user
