class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40
    
    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainer(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end=' ')
employee.displayNumberOfWorkingHours()

trainer = Trainer()
trainer.setNumberOfWorkingHours()
print("Number of working hours of trainer: ", end=' ')
trainer.displayNumberOfWorkingHours()
trainer.resetNumberOfWorkingHours()
print("Number of working hours of trainer after reset: ", end=' ')
trainer.displayNumberOfWorkingHours()
