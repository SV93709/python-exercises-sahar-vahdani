balance = int(input("موجودی حساب: "))
money = int(input("مبلغ برداشت: "))

if money <= 0:
    print("خطا: مبلغ برداشت باید بیشتر از صفر باشد")

elif money > balance:
    print("موجودی کافی نیست")

else:
    balance = balance - money
    print("برداشت با موفقیت انجام شد")
    print("موجودی جدید:", balance)