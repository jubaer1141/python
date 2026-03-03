#nested for loop

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)



for i in range(1, 4):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j)
    print()

#star pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()



#using break in nested loops
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break     #break only stopes the inner loop
    
        print(i, j)

#using continuie in nested lops
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)


#list inside list
students = [
    ["Jubaer", 22],
    ["Rafi", 21],
    ["Nabil", 23]
]

for student in students:
    for item in student:
        print(item)
    print("-----")



#nested dictionary style data
contacts = {
    "friends": ["Rafi", "Nabil"],
    "family": ["Father", "Mother"]
}

for group in contacts:
    print("Group:", group)
    for name in contacts[group]:
        print(" ", name)


#matrix 
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()