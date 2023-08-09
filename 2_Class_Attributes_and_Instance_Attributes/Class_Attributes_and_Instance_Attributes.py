class Employee:
    def employeeDetails(self):
        self.name = "Nguyễn Tuấn Anh"
        self.age = 21
        print(f"Hello, I'm {self.name} and I'm {self.age}")

employee = Employee()
employee.employeeDetails()
Employee.employeeDetails(employee)