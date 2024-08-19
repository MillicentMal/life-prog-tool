from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, email):
        self.email = email

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

admin = User("Admin")