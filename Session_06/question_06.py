# tamrin 6
sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)

customer_sales = {}

for customer, product, price in sales:

    if customer in customer_sales:
        customer_sales[customer] += price
    else:
        customer_sales[customer] = price


for customer, total in customer_sales.items():
    print(customer, "---→", total)


total_sales = sum(customer_sales.values())

print()
print("Total sales:", total_sales)
