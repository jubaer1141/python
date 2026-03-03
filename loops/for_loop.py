#for variable in iterable:
    # body of the loop

#iterable -> something you can loop through
#variable -> receives one item at a time


#
numbers = [10, 20, 30, 40]

for n in numbers:
    print(n)

##
text = "Python"

for ch in text:
    print(ch)

##range()
for i in range(1, 6):
    print(i)

##range() with step
for i in range(0, 10, 2):  #range(start, stop, step)
    print(i)    # 0 2 4 6 8



###
student = {
    "name": "Jubaer",
    "age": 22,
    "dept": "CSE"
}

for key in student:
    print(key, student[key])


###
student = {
    "name": "Jubaer",
    "age": 22,
    "dept": "CSE"
}

for key, value in student.items():
    print(key, "->", value)



numbers = [5, 10, 15, 20, 25]

for n in numbers:
    if n == 15:
        break
    print(n)



numbers = [5, 10, 15, 20, 25]

for n in numbers:
    if n == 15:
        continue
    print(n)




numbers = [2, 4, 6, 8]

for n in numbers:
    if n % 2 != 0:
        print("Odd found")
        break
else:
    print("All numbers are even")




#example

names = ["Rafi", "Tanim", "Jubaer", "Nabil"]

target = "Jubaer"
found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print("Name found")
else:
    print("Name not found")



##
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n * n)

print(squares)