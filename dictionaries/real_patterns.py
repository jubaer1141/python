#frequency counting
data = ["apple", "banana", "apple", "orange"]

freq = {}

for item in data:
    freq[item] = freq.get(item, 0) + 1

print(freq)


#grouping
students = [("CSE", "Jubaer"), ("EEE", "Ali"), ("CSE", "Rafi")]

group = {}

for dept, name in students:
    group.setdefault(dept, []).append(name)

print(group)
