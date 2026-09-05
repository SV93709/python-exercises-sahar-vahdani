#tamrin 3
s=input('Enter character:')
upper = 0
lower = 0
number = 0
space = 0
special = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        number += 1
    elif i == " ":
        space += 1
    else:
        special += 1
print('Upper:', upper)
print('Lowercas:', lower)
print('Number:', number)
print('Space:', space)
print('Special character:', special)
