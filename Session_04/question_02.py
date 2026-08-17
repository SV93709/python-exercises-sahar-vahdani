import random
while True:
    user = input("سنگ، کاغذ یا قیچی؟ ")
    if user == "exit":
        print("بازی تمام شد")
        break
    if user != "سنگ" and user != "کاغذ" and user != "قیچی":
        print("ورودی اشتباه است")
        continue
    computer_number = random.randint(1, 3)
    if computer_number == 1:
        computer = "سنگ"
    elif computer_number == 2:
        computer = "کاغذ"
    else:
        computer = "قیچی"
    print("انتخاب کامپیوتر:", computer)
    if user == computer:
        print("مساوی شد")
    elif user == "سنگ" and computer == "قیچی":
        print("شما بردید")
    elif user == "کاغذ" and computer == "سنگ":
        print("شما بردید")
    elif user == "قیچی" and computer == "کاغذ":
        print("شما بردید")
    else:
        print("کامپیوتر برد")