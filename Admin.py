class Admin:
    """
    Implements an Admin class
    Admin can:
    1. initiate registration for other users
    2. update their information
    3.

    """

    def __init__(self, email, password, first_name, last_name):
        super().__init__(email, password, first_name, last_name)
        

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








admin1 = Admin('josh@hater.com', 'wesbaby', 'Joshua', 'Momo')
print(admin1.email)
admin1.email = 'millicent'
print(admin1.email)
