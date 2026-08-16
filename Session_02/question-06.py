#tmrin 6

s=int(input("enter mablaq:"))
if s>1000000:
    p=s*0.85
elif s>=500000:
    p=s*0.90
else:
    p=s
print("mablaq:",p)

