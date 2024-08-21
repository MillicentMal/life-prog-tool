from admin import Admin
from user import User


def main():
    print_menu()
    # choice = input('Enter your choice: ')
    # if choice == "1":
    #     login_menu()

    while True:

        choice = input(f"Please choose an option: ")
        if choice == "3":
            break

        if choice == "1":
            login_state =  login_menu()

            while login_state:
                login_choice = input(f"Please choose an option: ")
                if login_choice == "1":



        # if int(choice) == 1:
        #     email = input("Enter your email: ")
        #     with open(file='user.txt', mode='a') as file:
        #         file.write(email)
        #     continue


def login_menu():
    email = input("Enter your email: ")
    if '@' in email and email.endswith('.com'):
        with open(file='user.txt', mode='r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
                if email in line:
                    password = input("Enter your password: ")
                    if password in line:
                        if "admin" in line:
                            print_admin_menu()
                            return True
                        elif "patient" in line:
                            print_patient_menu()
                            return True
            print("Email not found")
    else:
        print("Please enter a valid email")
    return 0




def print_menu():
    login_dict = {1: "Login", 2: "Complete Registration", 3: "Exit"}
    for key, value in login_dict.items():
        print(f"{key} {value}")


def print_admin_menu():
    interface_dict = {1: "Initiate Registration", 2: "Download User Files", 3: "Exit", 0: 'Main Menu'}
    for key, value in interface_dict.items():
        print(f"{key}: {value}")


def print_patient_menu():
    interface_dict = {1: "Complete Registration", 2: "View Profile", 3: "Update Profile",
                      4: "Exit", 0: 'Main Menu'}
    for key, value in interface_dict.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
