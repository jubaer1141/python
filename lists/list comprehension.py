#list = [expression for item in iterable]
#basic form
nums = [1, 2, 3, 4]
squares = [x * x for x in nums]
print(squares)  

#with condition

nums = [1, 2, 3, 4, 5, 6]
even = [x for x in nums if x % 2 == 0]
print(even)

#create list from range
data = [x for x in range(5)]
print(data)


#example
names = ["python", "java", "c"]
upper_names = [x.upper() for x in names]
print(upper_names)


