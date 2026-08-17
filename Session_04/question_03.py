password = input("رمز عبور را وارد کنید: ")

if len(password) == 8:

    if password[:4].isalpha() and password[4:].isdigit():
        print("معتبر")
    else:
        print("نامعتبر")

else:
    print("نامعتبر")