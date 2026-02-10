#When we assign multiple values to a tuple, it is called packing.)
#When we take tuple values into variables, it is unpacking.

t = (10, 20, 30)
a, b, c = t

print(a)
print(b)
print(c)


data = (1, 2, 3, 4, 5)
a, *b, c = data

print(a)   #1
print(b)   #[2, 3, 4] - became a list
print(c)   #5
