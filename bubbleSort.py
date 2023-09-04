# create a list
num = [12, 3, 42, 5, 77, 56, 89, 65]
print("Numbers before bubble sorting : ", num)
# find a length of list
n = len(num)


# function for bubble sort algorithm
def bubbleSort(num):
    for i in range(0, n-1):
        for j in range(n-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j]= num[j+1]
                num[j+1] = temp
    return num


print("Elements after bubble sorting : ", bubbleSort(num))
