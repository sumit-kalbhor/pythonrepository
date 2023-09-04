# create generator function
def number():
    yield 1
    yield 2
    yield "Hello World"


# for loop method
for i in number():
    print(i)

# x is a generator object
x = number()

# next method for iterating generator object
print(next(x))
print(next(x))
print(next(x))

