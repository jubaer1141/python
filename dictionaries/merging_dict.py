#using update
a = {"x": 1, "y": 2}
b = {"y": 5, "z": 3}

a.update(b)
print(a)


#way |
a = {"x": 1}
b = {"y": 2}

c = a | b
print(c)     #{'x': 1, 'y': 2}



#unpacking
a = {"x": 1}
b = {"y": 2}

c = {**a, **b}
print(c)
