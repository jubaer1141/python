text = "I am learning python"

print(text.find("python")) #14
#if find it return the the first letter cordinate

print(text.find("java")) #-1
#if not found it returns -1

print(text.rfind("o")) #18
print(text.rfind("gg"))  #-1


#--------find() vs rfind----------#
text= "hello world hello" #             h e l l o   w o r l d     h  e  l  l  o
#                                       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
print(text.find("hello"))   #0
print(text.rfind("hello"))  #12
#there are 2 hello 
# 1st start at 0
# 2nd start at 12
#


print(text.startswith("I")) #True
print(text.startswith("am")) #false
#check is the string start with given word


print(text.endswith("learning")) #false
print(text.endswith("python"))   #true
#check is the streing end with givven word




email = "mdjubayer1141@gail.com"

if email.endswith(".com"):
    print("Valid domain")
else:
    print("Invalid domain")