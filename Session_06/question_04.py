#tamrin 4
employees = {
    "E01": {"name": "Ali", "age": 28, "salary": 3000},
    "E02": {"name": "Sara", "age": 32, "salary": 4500},
    "E03": {"name": "Reza", "age": 25, "salary": 2800}
}

#bishtarin
b_salary = 0
b_name = ""
for i in employees:
    if employees[i]["salary"] > b_salary :
        b_salary = employees[i]["salary"]
        b_name = employees[i]["name"]
print("bishtarin :", b_name, "salary", b_salary)
print('______________________________________')
# avg salary
total = 0
count = 0
for i in employees:
    total = total + employees[i]["salary"]
    count = count + 1
avg = total / count
print(" avg salary: ", avg)
print('______________________________________')
#bishtar az 3000
print(" bishtar az 3000: ")
for i in employees:
    if employees[i]["salary"] > 3000:
        print(" ", employees[i]["name"], "-", employees[i]["salary"])
print('______________________________________')
#kamtarin
m_salary = 999999
m_name = ""
for i in employees:
    if employees[i]["salary"] < m_salary:
        m_salary = employees[i]["salary"]
        m_name = employees[i]["name"]
print(" kamtarin: ", m_name)