# match_case.py

choice = input("Enter a number (1-3): ")

match choice:
    case "1":
        print("Add contact")
    case "2":
        print("View contact")
    case "3":
        print("Exit")
    case _:
        print("Invalid choice")



num = int(input("Enter a number: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")



day = input("Enter day: ")

match day:
    case "Sat" | "Sun":
        print("Weekend")
    case "Mon" | "Tue" | "Wed" | "Thu":
        print("Working day")
    case _:
        print("Invalid day")



point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("On Y axis")
    case (x, 0):
        print("On X axis")
    case _:
        print("Somewhere else")




print("1. Add contact")
print("2. View contact")
print("3. Delete contact")
print("4. Exit")

choice = input("Enter your choice: ")

match choice:
    case "1":
        print("Add contact selected")
    case "2":
        print("View contact selected")
    case "3":
        print("Delete contact selected")
    case "4":
        print("Exit selected")
    case _:
        print("Invalid choice")