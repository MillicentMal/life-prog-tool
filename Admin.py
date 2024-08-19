class Admin:
    """
    Implements an Admin class
    Admin can:
    1. initiate registration for other users
    2. update their information
    3.

    """

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
    


admin1 = Admin('Joshua')
print(admin1.name)
admin1.name = 1
print(admin1.name)
