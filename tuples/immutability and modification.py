#immutability
#we cant change,add or move items in touple


#modify
t = (10, 20, 30)

temp = list(t)
temp[0] = 100
t = tuple(temp)
#tuple -> list -> modify -> tuple again

print(t)   #(100, 20, 30)


t = (5, 6)
print(t * 3)  #(5, 6, 5, 6, 5, 6)



t = (10, 20, 30)

print(20 in t)  #true
print(50 in t)  #False
