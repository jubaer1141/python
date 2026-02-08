#string[start : end]

string = "Python"

print(string[0:4])     # Pyth
print(string[2:6])     # thon
print(string[:3])      # Pyt
print(string[3:])      # hon
print(string[-4:-1])   # tho



#Slcing With Step
print(string[0:6:2])   #Pto

#(string[start : End : step])
#here start index 0------> start from o index
#End 6 -----------> Go up to 6 index ( 6 is not include)
#step 2 -----------> jump 2 step each time and take the value 


#another example:

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string[1:24:3])  #output "BEHKNWTWZ"
#BEHKNWTWZ
#start from 1 means B
#End at 24 means X
# jump 3 step so (B..E..H..K..N..Q..T..W)