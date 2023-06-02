import re

def password_validator(password, retry=True):
    pass_pattern = "^(?=.*?[0-9])(?=.*[a-z])(?=.*?[A-Z]).{8,}$"
    if re.match(pass_pattern, password):
        print("password is valid")
    else:
        print("password is invalid")
        if retry:
            password2 = input("Enter your password: ")
            password_validator(password2)


password1 = input("Enter your password: ")
password_validator(password=password1)
