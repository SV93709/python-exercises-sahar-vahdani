#tamin 1
while True:
    pas = True
    password = input('Enter password: ')
    if len(password) < 8:
        print('Password must contain at least 8 characters')
        pas = False

    elif password.isdigit() or password.isalpha():
        print('It must contain both letters and numbers')
        pas = False
    elif password.islower() or password.isupper():
        print('It must contain both uppercase and lowercase letters')
        pas = False

    elif not any(char in '@#$%' for char in password):
        print('Password must contain a special character')
        pas = False
    else :
        print('Successfully registered')
        break
        
    