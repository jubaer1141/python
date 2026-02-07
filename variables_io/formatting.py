x=input("enter a number: ")
y=float(x)
z=int(float(x))
print("Orginal:", x, type(x))
print("As float: ",y, type(y))
print("As int: ",z, type(z))


#fixing decimal place
cgpa=3.18818
print(f"{cgpa: .2f}")


#zero pading numbers
roll = 3
print(f"{roll:03}")


#formating large number with comma
amount=156484165165
print(f"{amount:,}")


#percentage
num=0.50
print(f"{num:.2%}")