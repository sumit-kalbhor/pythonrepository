# create a tuple
day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(day)

# print using index numbers

print(day[2])
print(day[1:5])
print(day[0:])
print(day[:4])

# access using loops
# for loop
for i in day:
    print(i)

# while loop

count = 0
while count < len(day):
    print(day[count])
    count += 1

# nested tuple and tuple methods

nested = (1, 2, (3, 4, 5), (6, 7), 8)
print(nested)
print(len(nested))
print(nested[2])
print(nested.index(2))
print(nested.count(1))
