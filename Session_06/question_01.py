#tamrin 1
products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 500,
    "headphone": 150,
    "mouse": 50
}

# 1. گران‌ترین محصول
expensive = max(products, key=products.get)
print(" gerantarin:", expensive)
print("price:", products[expensive])
print('____________________')

# 2. ارزان‌ترین محصول
cheap = min(products, key=products.get)
print("arzantarin:", cheap)
print("price:", products[cheap])

print('____________________')
# 3. میانگین قیمت محصولات
average = sum(products.values()) / len(products)
print("avg:", average)

print('____________________')
# 4. محصولاتی که قیمتشان بیشتر از 500 است
print("bish az 500 :")

for name, price in products.items():
    if price > 500:
        print(name, "→", price)
print('____________________')

# 5. مجموع قیمت تمام محصولات
total = sum(products.values())
print("total price:", total)
