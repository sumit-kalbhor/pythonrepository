# public => memberName
# protected => _memberName
# private => __memberName


class Car:
    # public attribute
    noOfWheels = 4

    # protected attribute
    _color = "White"

    # private attribute
    __yearOfManufacture = 2023


class Bmw(Car):
    def __init__(self):
        print("Color of car is : ", self._color)


car = Car()
print("No of wheels: ", car.noOfWheels)
bmw = Bmw()
print("Year of Manufacturing is : ", car._Car__yearOfManufacture)
