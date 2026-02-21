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