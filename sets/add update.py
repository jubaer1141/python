# add_update.py

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)


numbers = {1, 2, 3}
numbers.update([4, 5, 6])
print(numbers)



#if teh value exist already
numbers = {1, 2, 3}
numbers.add(2) 
print(numbers)   #{1, 2, 3}
#set ignore duplicates


#update with diff iterables
s = {1, 2}
s.update((3, 4))      # tuple
s.update({5, 6})      # set
s.update("78")        # string

print(s)     #{1, 2, 3, 4, 5, 6, '7', '8'}
#string is iterable each character is added
