#tamrin 2
inventory = {'apple': 20,'banana': 5,'orange': 0,'milk': 12,'bread': 0}

a = []
b = []

for p, q in inventory.items():
    if q > 0:
        a.append(p)
    else:
        b.append(p)
print('______________')
print('Available: ')
for i in a:
    print(f'  {i}')
    
print('______________')
print('\nOut of stock: ')
for i in b:
    print(f'  {i}')
print('______________')