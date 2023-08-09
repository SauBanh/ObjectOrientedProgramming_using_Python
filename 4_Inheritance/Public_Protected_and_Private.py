# Public => memberName
# Protected => _memberName
# Private => __memberName

class Car: 
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacturer = 2017 # _Car__yearOfManufacturer

class Bmw(Car):
    def __init__(self):
        print("Protected atribute color: " + self._color)

car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)

bmw = Bmw()
# print("Private attribute yearOfManufacturer: ", car.__yearOfManufacturer) is not work
print("Private attribute yearOfManufacturer: ", car._Car__yearOfManufacturer)