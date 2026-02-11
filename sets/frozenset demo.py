# frozenset demo

numbers = [1, 2, 3, 4]
f = frozenset(numbers)
print(f)
print(type(f))

#you cant add, remove from frezenset
#but you can use set operation

A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print(A | B)
print(A & B)


#example
permissions = frozenset(["read", "write"])

if "read" in permissions:
    print("Read allowed")
