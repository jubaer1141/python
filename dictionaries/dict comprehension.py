nums = [1, 2, 3, 4]
squares = {n: n*n for n in nums}  #{key_expr: value_expr for item in iterable if condition}

print(squares)  #{1: 1, 2: 4, 3: 9, 4: 16}



#with condition
even_squares = {n: n*n for n in nums if n % 2 == 0}

print(even_squares) #{2: 4, 4: 16}


#example
marks = {
    "Math": 85,
    "Physics": 78,
    "Programming": 92
}
passed = {k: v for k, v in marks.items() if v >= 80}

print(passed)


##
names = ["Jubaer", "Ali", "Rafi"]
name_len = {name.lower(): len(name) for name in names}

print(name_len)
