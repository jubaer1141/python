#membership
student = {
    "name": "Jubaer",
    "age": 22,
    "dept": "CSE"
}

print("name" in student)
print("cgpa" in student)


key = "email"

if key not in student:
    print("Email not found")
