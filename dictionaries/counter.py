from collections import Counter

text = "banana"

c = Counter(text)
print(c)


#most common
print(c.most_common(1))
