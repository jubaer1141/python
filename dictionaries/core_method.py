#setdefault()
profile = {
    "name": "Jubaer"
}

profile.setdefault("city", "Dhaka")

print(profile)

#setdefault() when key already exists
profile.setdefault("name", "Ali")

print(profile)
#existing key is NOT changed


#copy()
a = {
    "x": 1,
    "y": 2
}

b = a.copy()

b["x"] = 100

print("a:", a)
print("b:", b)



#fromkeys()
keys = ["math", "physics", "programming"]

marks = dict.fromkeys(keys, 0)

print(marks)


#building frequency dictionary
text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
