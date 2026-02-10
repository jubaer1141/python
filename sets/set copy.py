#copy()
a = {1, 2, 3}
b = a.copy()
b.add(10)

print("a:", a)
print("b:", b)



original = {"apple", "banana"}
backup = original.copy()
original.remove("apple")

print("original:", original)
print("backup:", backup)

