#keys()
d = {"a": 1, "b": 2}

k = d.keys()
print(k)

d["c"] = 3
print(k)
#view updates automatically


#items()
for k, v in d.items():
    print(k, v)
