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
