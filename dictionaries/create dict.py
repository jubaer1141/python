# create dict

student = {
    "name": "Jubaer",
    "age": 25,
    "department": "CSE"
}

print(student)        #{'name': 'Jubaer', 'age': 22, 'department': 'CSE'}
print(type(student))  #<class 'dict'>



#Create using dict()
student = dict(name="Hossain", age=25, dept="CSE")
print(student)



#Empty dictionary
data = {}
print(data)    #{}
print(type(data))

#Duplicate keys
info = {
    "name": "Jubaer",
    "name": "Ali",
    "age": 22
}

print(info)    #{'name': 'Ali', 'age': 22}

#creating from two lists

keys = ["id", "name", "dept"]
values = [101, "Jubaer", "CSE"]

student = dict(zip(keys, values))

print(student)
