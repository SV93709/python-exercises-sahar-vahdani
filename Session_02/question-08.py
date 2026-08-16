#tamrin 8
h=int(input("enter time:"))
if h < 0 or h > 23:
    print("error")
elif h < 12:
    print("AM")
elif h < 18:
    print("PASS AM")
else:
    print("PM")
