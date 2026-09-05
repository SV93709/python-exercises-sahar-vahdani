# tamrin 9
user = "sahar"
password = "1234"
a = 3
while a > 0:
    username = input("Username: ")
    user_password = input("Password: ")
    if username == user and user_password == password:
        print("Login successful")
        break
    else:
        a -= 1
        print("Wrong username or password")
        if a > 0:
            print("Attempts remaining:", a)
        else:
            print("You are blocked")

