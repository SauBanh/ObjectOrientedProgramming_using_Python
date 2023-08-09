# ObjectOrientedProgramming_using_Python

## Classes and Objects

```python
class Employee:
    name = "Sáu Bảnh" # is a properties
    designation = "Developer" # is a properties
    done_task_this_week = 6 # is a properties
    def hasAchievedTarget(self): # self is the default parameter and is used to access the class properties
        if self.done_task_this_week >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")

employeeOne = Employee() # object initialization

employeeOne.name
# employeeOne.hasAchievedTarget()
```

## Attributes and Methods

### Class Attributes and Instance Attributes

```python
class Employee:
    def employeeDetails(self):
        self.name = "Nguyễn Tuấn Anh"
        self.age = 21
        print(f"Hello, I'm {self.name} and I'm {self.age}")

employee = Employee()
employee.employeeDetails()
Employee.employeeDetails(employee)
```

### Parameters

```python
class Employee:
    def employeeDetails(self):
        self.name = "Nguyễn Tuấn Anh"
        self.age = 21
        print(f"Hello, I'm {self.name} and I'm {self.age}")

employee = Employee()
employee.employeeDetails()
Employee.employeeDetails(employee)
```

### Static Methods and Instance Methods

```python
class Employee:
    def employeeDetails(self):
        self.name = "Nguyen Tuan Anh"

    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()

```

### init() method - Create a fully initialised object

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Nnguyen Tuan Anh")
employeeTwo = Employee("Sau Banh")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()
```

1. What is an attribute?
    - An attribute is property that further defines a class
2. What is a method?
    - A method is a function within a class which can access all the attributes of a class and perform a specific task
3. What is a class attributes?
    - Class attributes are attributes that are shared across all instances of a class
    - Thay are created either as a part of the class or by using className.attributesName
4. What is an instance attribute?
    - Instance attributes are a attributes that are specific to each instance of a class
    - Thay are created using objectName.attributeName

## Abstraction and Encapsulation

### Performing Abstraction and Encapsulation in Python

```python
class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("========================")
        print("Available Book: ")
        for book in self.availableBooks:
            print()
            print(book)
        print("========================")
    def lendBook(self, requestedBook):
        print("========================")
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our list")
        print("========================")

    def addBook(self, returnedBook):
        print("========================")
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thanks you!")
        print("========================")

class Customer:
    def requestBook(self):
        print("========================")
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        print("========================")
        return self.book

    def returnBook(self):
        print("========================")
        print("Enter the name of a book Which you are returning: ")
        self.book = input()
        print("========================")
        return self.book

library = Library(['Think and Grow Rich', 'Who will cry when you die', 'For one more day'])

customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoise = int(input())
    if userChoise == 1:
        library.displayAvailableBooks()
    elif userChoise == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoise == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoise == 4:
        quit()
```

### Inheritance

```python
class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contact_Details(self):
        print("To contact us, log on to ", self.contactWebsite)

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacturer = 2017

    def manufacturerDetails(self):
        # print("This Macbook was manufacturer in the year {} by {}".format(self.yearOfManufacturer, self.manufacturer))
        print(f"This Macbook was manufacturer in the year {self.yearOfManufacturer} by {self.manufacturer}")

macbook = Macbook()
macbook.manufacturerDetails()
macbook.contact_Details()
```

### Performing a Multiple Inheritance in Python

```python
class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    website = "www.apple.com"
    name = "Apple"

class Macbook(Apple, OperatingSystem):
    def __init__(self):
        if self.multitasking:
            print(f"This is multi tasking system. Visit {self.website} for more details")
            print(f"Name: {self.name}")
macBook = Macbook()
```

`Note: it will give priority to the first inherited parameter`

### Performing a Multilevel Inheritance in Python

```python
class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print(f"This guitar consists of {self.numberOfStrings} strings. It is made of {self.typeOfWood} and it can play {self.numberOfMajorKeys} keys")

guitar = Guitar()
```

### Public, Protected and Private - Naming Conventions in Python

`Public => memberName`
`Protected => _memberName`
`Private => __memberName`

```python
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
```
