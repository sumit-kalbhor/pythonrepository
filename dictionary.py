# create a dictionary : stores a key value pair
student = {1: "Sumit", 2: "Sujit", 3: "Apurba", 4: "Rahul", 5: "Divya"}
print(student)
print(student[2])

# in and not in
print(1 in student)
print(1 not in student)


# keys() method

print(student.keys())

for key in student.keys():
    print(key)

# values() method

print(student.values())

for value in student.values():
    print(value)

# items() method : it prints data as key value pair in tuple formate

print(student.items())

for key, value in student.items():
    print(key, value)

# get() method

print(student.get(1, "1 is not present in a dictionary"))

# len : to find a length of a dict

print(len(student))

# pop() and popitem()

print(student.popitem())
print(student)

print(student.pop(4))
print(student)

# setdefault() to add a key value in a dict

student.setdefault(4, "Sagar")
print(student)

# clear() to clear a dict

student.clear()
print(student)


