from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role 
        
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' in value and value.endswith('.com'):
            self._email = value
        else:
            print("Please enter a valid email.")

    @email.deleter
    def email(self):
        del self._email

    @property
    def password(self):
        return self._password
        # return 'For security reasons you can not see this password'

    @password.setter
    def password(self, password):
        # password = input("Enter your password: ")
        # confirm_password = input("Enter password again: ")

        if len(password) > 8 and password.isalnum():
            self._password = password
            return self._password
        else:
            print("Wrong password!")

    # methods

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def registration(self, email):
        pass
