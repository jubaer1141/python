#heavily used in backend and APIs


#dict -> JSOn
import json

student = {"name": "Jubaer", "dept": "CSE"}

s = json.dumps(student)
print(s)


#JSON-> dict
import json

data = '{"name": "Jubaer", "dept": "CSE"}'

obj = json.loads(data)
print(obj)
print(type(obj))
