A = {1, 2}
B = {1, 2, 3, 4}

#subset-> issubset()
print(A.issubset(B))

#superset-> issuperset()
print(B.issuperset(A))

#disjoint-> isdisjoint()
C = {10, 20}
print(A.isdisjoint(C))

#example
club_A = {"Jubaer", "Ali"}
club_B = {"Ali", "Rafi"}

print("All A in B?", club_A.issubset(club_B))
print("Any common?", not club_A.isdisjoint(club_B))

print(A <= B)   # subset
print(B >= A)   # superset
