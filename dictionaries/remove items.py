#pop(key)
# remove_items.py

student = {
    "name": "Jubaer",
    "age": 22,
    "dept": "CSE"
}

removed = student.pop("age")

print("Removed:", removed)
print(student)


#popitem()
student = {
    "name": "Jubaer",
    "age": 22,
    "dept": "CSE"
}

item = student.popitem() #removes the last inserted item

print(item)
print(student)


#del

del student["age"]
print(student)


#clear()
student.clear()
print(student)

