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

    def registration(self, email):
        new_person = Admin(email, 'ghjkluyhfiyghbjrfdsin')
        return new_person
        








admin1 = Admin('josh@hater.com', 'wesbaby78')

admin1.password = "carolbaby789"

print(admin1.registration('mimi@gmail.com').__dict__)
