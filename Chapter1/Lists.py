# A list is an ordered collection of zero or more references to Python data objects
# We can see this by printing the id's of each object


my_List = ['a', True, 50]

for i in my_List:
    print(id(i))
print(id(my_List))

my_List.append(1000)  # append adds the element to the END
print(my_List)
my_List.pop(2)  # Pop removes the element from the END, unless position is specified
print(my_List)
my_List.append(1000)
print(my_List)
print(my_List.count(1000))
my_List.remove(1000)
print(my_List)
