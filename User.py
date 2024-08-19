from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self.name = name

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
