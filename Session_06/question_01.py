#tamrin 1
products = {"laptop": 1200,"phone": 800,"tablet": 500,"headphone": 150,"mouse": 50}

#gerantarin
g=max(products, key=products.get)
print('gerantarin mahsol: ',g)
print('qeymat: ',products[g])

print('___________________________')

#arzantarin 
c=min(products, key=products.get)
print('arzantrin mahsol: ',c)
print('qeymat: ',products[c])

print('___________________________')
 
#avg
avg=sum(products.values())// len(products)
print('avg: ',avg)

print('___________________________')

#bish az 500
print('bish az 500: ')
for name,p in products.items():
    if p>500:
        print(name,p)

print('___________________________')

#sum mahsolat
s=sum(products.values())
print('sum mablaq: ',s)

