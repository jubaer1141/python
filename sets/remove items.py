#removed()
s = {10, 20, 30}
s.remove(20)
print(s)



#discard()
s = {10, 20, 30}
s.discard(100)
print(s)



#pop()
s = {1, 2, 3, 4}
removed = s.pop()
print("Removed:", removed)
print("Set now:", s)



#clear()
s = {5, 6, 7}
s.clear()
print(s)



#example
students = {"Ali", "Jubaer", "Rafi"}
name = "Hasan"
if name in students:
    students.remove(name)
else:
    print("Student not found")

print(students)
