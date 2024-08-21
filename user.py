from abc import ABC, abstractmethod
import hashlib
from roles_enum import Role


class User(ABC):
    """A formal abstract class that enforces strict inheritance on the sub-classes."""
    def __init__(self, first_name, last_name, email, password, role):
        self.first_name = first_name
        self.last_name = last_name
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
        """Getter method for password."""
        return self._password
        # return 'For security reasons you can not see this password'

    @password.setter
    def password(self, password):
        """Setter method for password attr. It allows 
        a strict setting of password in the object."""
        # password = input("Enter your password: ")
        # confirm_password = input("Enter password again: ")

        if len(password) > 8 and password.isalnum():
            self._password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return self._password
        else:
            print("Wrong password!")

    # methods
    # @staticmethod
    # def hash_password(password):
    #     return hashlib.sha256(password.encode('utf-8').hexdigest())
    
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def registration(self, email):
        pass
    
    @abstractmethod
    def view_profile(self):
        pass
    
    @abstractmethod
    def update_profile(self):
        pass

    def __str__(self) -> str:
        return super().__str__()