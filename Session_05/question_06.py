#tamrin 6
s=input('enter word: ')
w=['hack','fraud','scam','password','attack']
for i in w:
    x=s.lower().split().count(i)
    if x > 0:
        print(i,':',x)

