number1 = int(input("عدد اول: "))
number2 = int(input("عدد دوم: "))

operator = input("عملگر را وارد کنید: ")

if operator == "+":
    result = number1 + number2

elif operator == "-":
    result = number1 - number2

elif operator == "*":
    result = number1 * number2

elif operator == "/":
    result = number1 / number2

else:
    result = "عملگر اشتباه است"

print("نتیجه:", result)