from User import User

class Admin(User):
    """
    Implements an Admin class
    Admin can:
    1. initiate registration for other users
    2. update their information
    3.

    """

    def __init__(self, email, password):
        super().__init__(email, password)


    def login(self):
        pass

    def registration(self):
        pass








admin1 = Admin('josh@hater.com', 'wesbaby78')

admin1.password = "carolbaby789"
