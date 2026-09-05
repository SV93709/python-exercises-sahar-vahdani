#tamrin 7
s=input('enter word: ')
x=''
c=1
for i in range(len(s)):
    if i< len(s)-1 and s[i]==s[i+1]:
        c+=1
    else:
        x+=s[i]+str(c)
        c=1
print(x)
