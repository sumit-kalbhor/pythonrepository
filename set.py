# create a sets
# set can not store duplicate values

number = {1, 2, 3, 4, 5, 2, 1}
number_1 = set({"one", "two", "three", "four", "one"})
print(number)
print(number_1)


# for loop to get values

for i in number:
    print(i)

# set methods

print(1 in number)
print(6 not in number)
print(len(number))

# add() method
number.add(6)
print(number)

# remove() method
number.remove(6)
print(number)

# discard() method
number.discard(5)
print(number)

# copy() method
copyset = number.copy()
print(copyset)
print(copyset is number)

# union method used to combine 2 sets

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8,9,0}
set3 = set1.union(set2)
print(set3)

# intersection method

set4 = set1.intersection(set2)
print(set4)

# difference method

set5 = set1.difference(set2)
print(set5)
