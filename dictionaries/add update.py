# add a new key

student = {
    "name": "Jubaer",
    "age": 22
}
student["dept"] = "CSE"
print(student)

#update an existing key
student["age"] = 23   #prevous value replaced
print(student)   



#update() with multiple items
student.update({
    "university": "DIU",
    "semester": 7
})
print(student)


#update from another dict
extra = {
    "club": "Programming Club",
    "city": "Dhaka"
}

student.update(extra)

print(student)

