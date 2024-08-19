class Admin:
    """
    Implements an Admin class
    Admin can:
    1. initiate registration for other users
    2. update their information
    3.

    """
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        else:
            self._name = name


admin1 = Admin('Joshua')
print(admin1.name)
admin1.name = 1
print(admin1.name)
