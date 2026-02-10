#remove
numbers = [10, 20, 30, 40, 43, 50]
numbers.remove(43)
print(numbers)   #[10, 20, 30, 40, 50]


numbers = [10, 20, 30, 40, 43, 50, 10, ]
numbers.remove(10)
print(numbers)   #[20, 30, 40, 43, 50, 10]
#-remove only first match 





#pop()
nums = [10, 20, 30, 10, 10]
x = nums.pop()
#pop() removes last item and stores it in x.
print(x)     #10
print(nums)  #[10, 20, 30, 10]



#pop(index)
numbers = [10, 20, 30, 40, 43, 50, 20, 60 ]
x = numbers.pop(1)
print(x)         #20
print(numbers)   #[10, 30, 40, 43, 50, 20, 60]


#del
numbers = [10, 20, 30, 40, 43, 50, 20, 60 ]
del numbers[1] 
print(numbers)    #[10, 30, 40, 43, 50, 20, 60]


#also we can change item
nums = [1, 2, 3]
nums[0] = 100
print(nums)       #[100, 2, 3]
