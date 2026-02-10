#create
t = (10, 20, 30)
print(t)
print(type(t))


t1 = (10)
t2 = (10,)
print(type(t1))   #(10)   -> not a tuple
print(type(t2))   #(10,)  -> tuple


student = ("Jubaer", 22, 3.50, True)
print(student)


#accessing
t = ("a", "b", "c", "d")
print(t[0])
print(t[-1])


t = (10, 20, 30, 40, 50)
print(t[1:4])
