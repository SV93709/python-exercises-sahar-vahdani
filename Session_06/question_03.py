#tamin 3
{'p': 1,'r': 2,'o': 1,'g': 2,'a': 1,'m': 2,'i': 1,'n': 1}

def char(s):
    a = {}
    for i in s:
        if i.isalpha():  
            i = i.lower()  
            a[i] = a.get(i, 0) + 1
    return a

x = input('enter text: ')
m = char(x)
print(m)

