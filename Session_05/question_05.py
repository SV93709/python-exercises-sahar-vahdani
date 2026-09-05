#tamrin 5
k=input('enter jomle: ')
w=k.split()
long=w[0]
for i in k:
    if len(w)>len(long):
        long=w
print(long)
print('long word:', len(long))

