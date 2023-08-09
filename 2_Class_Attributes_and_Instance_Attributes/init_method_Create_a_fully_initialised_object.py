class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Nnguyen Tuan Anh")
employeeTwo = Employee("Sau Banh")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()