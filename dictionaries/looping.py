# loop through key

student = {
    "name": "Jubaer",
    "age": 22,
    "dept": "CSE"
}

for key in student:
    print(key)

#Loop through values
for value in student.values():
    print(value)

#loop through key and values
for key, value in student.items():
    print(key, "=>", value)


#example
marks = {
    "Math": 85,
    "Physics": 78,
    "Programming": 92
}

total = 0

for m in marks.values():
    total += m

print("Total:", total)




passed = {}

for subject, mark in marks.items():
    if mark >= 80:
        passed[subject] = mark

print(passed)
