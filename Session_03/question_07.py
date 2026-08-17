color1 = input("رنگ اول: ")
color2 = input("رنگ دوم: ")
color3 = input("رنگ سوم: ")

if color1 == color2 and color2 == color3:
    print("هر سه رنگ یکسان هستند")

elif color1 == color2 or color1 == color3 or color2 == color3:
    print("دو رنگ یکسان هستند")

else:
    print("رنگ ها یکسان نیستند")