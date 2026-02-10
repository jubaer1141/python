#using loop
s = {10, 20, 30}

for item in s:
    print(item)

#converting to list
s = {100, 200, 300}
temp = list(s)
print(temp)
print(temp[0])


#set comprehension
s = {1, 2, 3, 4, 5}
even_numbers = {x for x in s if x % 2 == 0}
print(even_numbers)


#example
names = {"Jubaer", "Ali", "Rafi", "Hasan"}

short_names = {name for name in names if len(name) <= 4}

print(short_names)
