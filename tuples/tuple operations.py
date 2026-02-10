#concatenation (+)
a = (1, 2)
b = (3, 4)

c = a + b
print(c)


t1 = ("Jubaer",)
t2 = ("CSE", "DIU")

info = t1 + t2
print(info)


#repetation(*)

t = (10, 20)
print(t * 3)      #(10, 20, 10, 20, 10, 20)



pattern = ("A", "B")
new_pattern = pattern * 2
print(new_pattern)   #('A', 'B', 'A', 'B')



#membership operation(in, not in)
t = (10, 20, 30)

print(20 in t)
print(50 in t)


names = ("python", "java", "c")

if "python" in names:
    print("Python is present")


#comparison of tuples (== , != , < , > , <= , >=)

a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)


a = (1, 5)
b = (2, 1)
print(a < b)


#example
allowed = ("admin", "manager", "staff")

user = "admin"

if user in allowed:
    print("Access granted")
else:
    print("Access denied")
