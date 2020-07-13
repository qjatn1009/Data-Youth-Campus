class Customer:
    def __init__(self, name ="", gender="", email="", birthday=""):
        self.__name = name
        self.__gender = gender
        self.__email = email
        self.__birthday = birthday
    
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email

    def set_birthday(self, birthday):
        self.__birthday = birthday
    
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_birthday(self):
        return self.__birthday