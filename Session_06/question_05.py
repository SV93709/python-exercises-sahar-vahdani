#tamrin 5
students = {
    "Ali": [18, 17, 20],
    "Sara": [15, 19, 18],
    "Reza": [12, 14, 10],
    "Mina": [20, 20, 19]
}

best_name = ""
best_average = 0
for i in students:
    scores = students[i]     
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    if average >= 15:
        status = "Passed"
    else:
        status = "Failed"
    print(i)
    print("Average:", round(average, 2))
    print("Status:", status)
    print() 
    if average > best_average:
        best_average = average
        best_name = i
    print('_________________')
print("بهترین دانش آموز:", best_name)
print("بالاترین میانگین:", round(best_average, 2))
