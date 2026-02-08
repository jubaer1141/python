#Arithmetic Operators = + - * / % // **

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
rem = num1 % num2       #Remainder
Fdiv = num1 // num2     #Floor division
exp = num1 ** num2      #power


print("Addition: ",add)
print("Substraction: ",sub)
print("Multiplication: ",mul)
print("Division: ",div)
print("Remainder: ",rem)
print("Floor division: ",Fdiv)
print("Power: ",exp)


x=5+2*3**2//4-1
print(x)