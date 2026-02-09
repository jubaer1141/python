#remove
numbers = [10, 20, 30, 40, 43, 50]
numbers.remove(43)
print(numbers)   #[10, 20, 30, 40, 50]


numbers = [10, 20, 30, 40, 43, 50, 10, ]
numbers.remove(10)
print(numbers)   #[20, 30, 40, 43, 50, 10]
#-remove only first match 



#pop(index)
numbers = [10, 20, 30, 40, 43, 50, 20, 60 ]
numbers.pop(1)
print(numbers)   #[10, 30, 40, 43, 50, 20, 60]


#del
numbers = [10, 20, 30, 40, 43, 50, 20, 60 ]
del numbers[1] 
print(numbers)    #[10, 30, 40, 43, 50, 20, 60]
