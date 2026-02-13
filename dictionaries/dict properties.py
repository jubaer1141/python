#keys must be immutable
good = {
    1: "one",
    "name": "Jubaer",
    (1, 2): "tuple key"
}
print(good)


#Values can be any type
data = {
    "name": "Jubaer",
    "marks": [80, 90, 85],
    "address": {"city": "Dhaka"}
}
print(data)



#Insertion order example
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d)
