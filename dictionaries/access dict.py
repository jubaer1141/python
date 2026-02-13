# 1. dict[key]
#dict.get(key)

#Using square brackets-[]
student = {
    "name": "Jubaer",
    "age": 22
}

print(student["name"])


#Using get()
print(student.get("name"))


#get() for missing key
print(student.get("cgpa"))  #None



#get() with default value
print(student.get("cgpa", 0.0))  #0.0
#if key not found
#return default value



#Example
profile = {
    "username": "jubaer",
    "email": "jubaer@gmail.com"
}

phone = profile.get("phone")

if phone is None:
    print("Phone number not added")



key = "email"

if key in profile:
    print(profile[key])
else:
    print("Key not found")
