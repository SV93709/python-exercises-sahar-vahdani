#tamrin 4
s= input('enter jomle: ')
k=s.split()
most_k=""
max_c=0
for i in k:
    count=k.count(i)
    if count>max_c:
        max_c=count
        most_k=i
print(most_k,':',max_c)

