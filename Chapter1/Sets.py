mySet = {3, 6, "cat", 4.5, False}

# |  returns a new set with all the elements in both sets
# &  returns a new set with only those elements common to both  (inner join)
# -  returns a new set with all those elements unique to the first set (left join)
# <=  asks whether all elements of the first set are in the second set


yourSet = {99, 3, 100}

newSet = mySet | yourSet
print(newSet)

newSet = mySet & yourSet
print(newSet)

newSet = mySet - yourSet
print(newSet)

print(mySet <= yourSet)
