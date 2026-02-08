#is
#is not

#use to check two  variables refer to the same obj.

a=[1,2,3]
b=a
c=[1,2,3]
d=[1,2,4]

print(a is b)
print(a is c)
print(a is not c)
print(a is d)