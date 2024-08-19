from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

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
        return 'For security reasons you can not see this password'

    @password.setter
    def password(self, password):
        if validate_password(password):
            self._password = password

    # methods

    @abstractmethod
    def user(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def registration(self, email):
        pass
