import random

number = random.randint(1, 10)

guess = int(input("حدس بزن: "))

while guess != number:

    if guess < number:
        print("عدد بزرگتر است")

    else:
        print("عدد کوچکتر است")

    guess = int(input("دوباره حدس بزن: "))

print("آفرین! درست حدس زدی")