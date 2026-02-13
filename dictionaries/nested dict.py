# nesteddict

students = {
    "S1": {
        "name": "Jubaer",
        "dept": "CSE"
    },
    "S2": {
        "name": "Ali",
        "dept": "EEE"
    }
}

print(students)


#Access nested values
print(students["S1"]["name"])    #first access S1 dictionary then access its "name"



#Update nested value
students["S1"]["dept"] = "Software Engineering"

print(students["S1"])

#Loop nested dictionary
for sid, info in students.items():
    print(sid, info["name"], info["dept"])


#safe access
name = students.get("S3", {}).get("name")

print(name)
