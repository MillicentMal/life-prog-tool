from admin import Admin
from user import User

def main():
    admin1 = Admin("josh@email.com", "bestbaby12")
    print(admin1.role)
    

if __name__ == "__main__":
    main()