name=input("Enter your name: ")
print("Your name is",name)


#using f-string
age=input("Enter your age: ")
print(f'Your age is {age}')

#using f-string with multiples values
print(f"Ok, I understad your name is {name} and your age is {age}")


#multiple input with space separator
x, y = input("Enter 2 number : ").split()
x = int(x)
y = int(y)
print(f"sum = {x+y}")