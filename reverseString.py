
# using extended slice

def reverse():
    name = "Sumit Kalbhor"
    print(str(name[::-1]))


reverse()

# using for loop

name = input("Enter a name : ")
reverse = ""

for i in range(len(name) -1, -1, -1):
    reverse += name[i]

print(reverse)

