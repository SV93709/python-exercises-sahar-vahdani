#tamrin 8
s = input("Enter a text: ")
total_characters = len(s)
w = s.split()
total_words = len(w)
letters = 0
digits = 0
spaces = 0
uppercase = 0
lowercase = 0

for i in s:
    if i.isalpha():
        letters += 1
    if i.isdigit():
        digits += 1
    if i == " ":
        spaces += 1
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase += 1
longest = w[0]

for j in w:
    if len(j) > len(longest):
        longest = j
shortest = w[0]

for j in w:
    if len(j) < len(shortest):
        shortest = j
most_char = ""
max_char_count = 0
for i in s:
    if i != " ":
        c = s.count(i)
        if c > max_char_count:
            max_char_count = c
            most_char = i
most_word = ""
max_word_count = 0

for j in w:
    c = w.count(j)
    if c > max_word_count:
        max_word_count = c
        most_word = j
print("Total characters:", total_characters)
print("Total words:", total_words)
print("Total letters:", letters)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total uppercase:", uppercase)
print("Total lowercase:", lowercase)
print("Longest word:", longest)
print("Shortest word:", shortest)
print("Most repeated character:", most_char)
print("Most repeated word:", most_word)
