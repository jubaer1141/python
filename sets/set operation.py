A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#union
print(A | B)
print(A.union(B))

#intersection
print(A & B)
print(A.intersection(B))

#difrence
print(A - B)
print(A.difference(B))

#symmentrirc diffrence
print(A ^ B)
print(A.symmetric_difference(B))



#example
python_students = {"Jubaer", "Ali", "Rafi"}
java_students   = {"Ali", "Hasan"}

print("All students:", python_students | java_students)
print("Both courses:", python_students & java_students)
print("Only python:", python_students - java_students)
print("Only one course:", python_students ^ java_students)
