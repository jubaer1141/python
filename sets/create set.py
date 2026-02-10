# create set [{}, set()]

#{}
numbers = {1, 2, 3, 4, 4, 2}

print(numbers)     #{1, 2, 3, 4} - set remove duplicates automatically
print(type(numbers)) #<class 'set'>

#set()
names = set(["Ali", "Jubaer", "Rahim", "Ali"])

print(names)



#empty set

#a = {}
#print(type(a))  #<class 'dict'>

#Correct way
b = set()
print(type(b))  #<class 'set'>



#example
text = "banana"

char_set = set(text)

print(char_set)  #{'b', 'a', 'n'}
#set keeps only unique characters