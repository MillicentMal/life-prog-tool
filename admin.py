import uuid

from user import User
from patient import Patient
from roles_enum import Role


class Admin(User):
    """
    Implements an Admin class
    Admin can:
    1. initiate registration for other users
    2. update their information
    3.

    """

    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password, role=Role.ADMIN)

    def login(self):
        pass

    def update_profile(self):
        pass

    def view_profile(self):
        pass

    def registration(self, email):
        return email, str(uuid.uuid4())


# admin1 = Admin('Test', 'Admin', 'test@testing.com', 'password123')
# email = input('Enter the email: ')
# print(admin1.registration(email))
