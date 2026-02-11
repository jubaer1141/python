## set_comprehension

numbers = {1, 2, 3, 4, 5, 6}
even_numbers = {n for n in numbers if n % 2 == 0}
print(even_numbers)

nums = {1, 2, 3, 4}
squares = {n * n for n in nums}
print(squares)


names = {"Jubaer", "Ali", "Rafi", "Hasan"}
short_names = {name.lower() for name in names if len(name) <= 4}
print(short_names)


emails = {"a@gmail.com", "b@yahoo.com", "c@gmail.com"}
gmail_users = {email for email in emails if email.endswith("gmail.com")}
print(gmail_users)
