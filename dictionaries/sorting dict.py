#sort by key

marks = {
    "Math": 85,
    "Physics": 78,
    "Programming": 92
}
sorted_by_key = dict(sorted(marks.items()))

print(sorted_by_key)


#sort by values
sorted_by_value = dict(sorted(marks.items(), key=lambda item: item[1]))

print(sorted_by_value)



# sorted in descending order
sorted_desc = dict(
    sorted(marks.items(), key=lambda item: item[1], reverse=True)
)
print(sorted_desc)


#sorted by ranking
ranking = sorted(marks.items(), key=lambda x: x[1], reverse=True)

for subject, mark in ranking:
    print(subject, mark)
