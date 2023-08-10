from abc import ABCMeta, abstractmethod

class Shaqe(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shaqe):
    side = 4
    def area(self):
        print("Area of square: ", self.side * self.side)

class Rectangle(Shaqe):
    width = 5
    length = 10
    def area(self):
        print("Area of rectangle: ", self.width * self.length)

square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
# shape = Shaqe()