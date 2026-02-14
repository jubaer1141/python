#
from collections import defaultdict

marks = defaultdict(int)

marks["math"] += 1
marks["math"] += 1
marks["physics"] += 1

print(marks)


##
from collections import defaultdict

students = [("CSE", "Jubaer"), ("EEE", "Ali"), ("CSE", "Rafi")]

group = defaultdict(list)

for dept, name in students:
    group[dept].append(name)

print(group)
