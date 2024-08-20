from user import User
from roles_enum import Role

class Patient(User):
    def __init__(self, email, password):
        super().__init__(email, password, role=Role.PATIENT)

    def registration(self, email):
        pass