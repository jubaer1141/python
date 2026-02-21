# nested_if_else

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 40:
    if attendance >= 75:
        print("Pass and allowed for final")
    else:
        print("Pass but attendance shortage")
else:
    print("Fail")


username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")