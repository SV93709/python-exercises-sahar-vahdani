x = input("یک رشته وارد کنید: ")

length = len(x)

if length % 2 == 0:
    print(x[:length // 2])
else:
    print(x[length // 2:])