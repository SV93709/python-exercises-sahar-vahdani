#tamrin 9
products = {
    "P01": ("Laptop", 1200, 5),
    "P02": ("Phone", 800, 0),
    "P03": ("Tablet", 500, 12),
    "P04": ("Mouse", 50, 25),
    "P05": ("Keyboard", 100, 0)
}

# 1. محصولات موجود
print("Available products:")

for code, (name, price, stock) in products.items():
    if stock > 0:
        print(name)


# 2. محصولات ناموجود
print("\nUnavailable products:")

for code, (name, price, stock) in products.items():
    if stock == 0:
        print(name)


# 3. ارزش موجودی هر محصول
print("\nInventory value:")

inventory_values = {}

for code, (name, price, stock) in products.items():
    value = price * stock
    inventory_values[code] = value
    print(name, "→", value)


# 4. محصول دارای بیشترین ارزش موجودی
max_product = max(inventory_values, key=inventory_values.get)

print("\nProduct with highest inventory value:")
print(products[max_product][0], "→", inventory_values[max_product])


# 5. ارزش کل انبار
total_inventory = sum(inventory_values.values())

print("\nTotal inventory value:", total_inventory)