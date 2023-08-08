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