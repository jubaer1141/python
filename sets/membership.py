# membership

students = {"Jubaer", "Ali", "Rafi"}
print("Ali" in students)
print("Hasan" in students)
print("Hasan" not in students)


#example
allowed_users = {"admin", "staff", "manager"}
user = "staff"
if user in allowed_users:
    print("Access granted")
else:
    print("Access denied")

#Access granted



email_domains = {"gmail.com", "yahoo.com", "outlook.com"}
email = "mdjubayer1141@gmail.com"
domain = email.split("@")[1]
print(domain in email_domains)
#True
