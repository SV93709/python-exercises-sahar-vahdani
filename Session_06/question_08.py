#tamrin 8
users = [
    ("Ali", 25, "Python"),
    ("Sara", 30, "Java"),
    ("Reza", 22, "Python"),
    ("Mina", 28, "C++"),
    ("John", 35, "Python"),
    ("David", 30, "Java")
]

groups = {}

for name, age, language in users:

    if language in groups:
        groups[language].append(name)
    else:
        groups[language] = [name]

print(groups)
