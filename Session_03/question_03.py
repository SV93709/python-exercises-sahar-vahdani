sum_number = 0

for i in range(1, 11):

    if i % 2 == 0:
        result = i * 5
        print(i, "* 5 =", result)

    else:
        result = i + 5
        print(i, "+ 5 =", result)

    sum_number = sum_number + result

print("مجموع:", sum_number)