# read a file in python

file = open('methods.py', 'r')

for i in file:
    print(i)

# create a new file and append data into file
file1 = open('tutorial.txt', 'a+')
file1.write("Hello Python \t")
file1.close()

# read a file
file1 = open('tutorial.txt', 'r')

for i in file1:
    print(i)
