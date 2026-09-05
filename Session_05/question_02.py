#tamrin 2
s=input('enter character:')
x = ""
for i in s:
    if not x or i != x[-1]:
        x += i
print(x)