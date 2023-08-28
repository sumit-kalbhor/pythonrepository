# create a list
int_list = [1, 2, 3, 4]
print(int_list)

mixed_list = [10.00, "Sumit", 1, True]
print(mixed_list)

# list() function creates a list
name = list("SUMIT")
print(name)

# in or not in operators
print('S' in name)
print('K' in name)
print('K' not in name)

str_list = ["one", "two", "three"]
print(str_list[1])

# list slicing

sliced = [1, 2, 3, 4, 5, 6]
print(sliced[2:4])
print(sliced[0:])


# update a list using index numbers

sliced[1] = 10
sliced[2:4] = [11, 12]
print(sliced)
print(sliced[3])

# create empty list 

empty_list =[]
print(empty_list)

# del  : deletes item using index number

colors = ["red", "green", "yellow", "orange", "white", "blue"]
print(colors)
del colors[0]
print(colors)

# remove() method : removes element using value

colors.remove("green")
print(colors)

# append : append method is used to add elements in a list

colors.append("red")
colors.append("green")
print(colors)

# insert() method : inserts elements using index number

colors.insert(0, "grey")
print(colors)

# sort : used to sort list

colors.sort()
print(colors)

# reverse = True : write elements in a reverse order
colors.sort(reverse=True)
print(colors)

# index() method to find out  index number of a value

print(colors.index("green"))


