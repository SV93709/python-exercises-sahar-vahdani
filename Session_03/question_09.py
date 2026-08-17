numbers = []

for i in range(10):
    number = int(input("عدد را وارد کنید: "))
    numbers.append(number)

print("اعداد منفی:")

for number in numbers:
    if number < 0:
        print(number)