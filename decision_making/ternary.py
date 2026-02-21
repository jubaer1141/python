#Syntax: value_if_true if condition else value_if_false

#basic if else:
age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"


#same thing with ternary:
#
age = int(input("Enter age: "))

status = "Adult" if age >= 18 else "Minor"

print(status)

##
a = 10
b = 20

max_value = a if a > b else b

print(max_value)