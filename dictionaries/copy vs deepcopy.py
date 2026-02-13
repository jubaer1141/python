##----------------shallow copy-------------------##
a = {
    "marks": [80, 90]
}

b = a.copy()

b["marks"].append(100)

print("a:", a)
print("b:", b)

#outer dict is copied
#inner list is still shared


##-------------------deep copy-------------------##

import copy

a = {
    "marks": [80, 90]
}

b = copy.deepcopy(a)

b["marks"].append(100)

print("a:", a)
print("b:", b)

#fully independent copy