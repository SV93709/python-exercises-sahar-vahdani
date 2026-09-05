#tamrin 10
s1 = input("Sentence 1: ")
s2 = input("Sentence 2: ")
w1 = s1.split()
w2 = s2.split()

for i in w1:
    if i in w2:
        print(i)