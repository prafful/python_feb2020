class Employee:
    count = 0
    def __init__(self, name, salary):
        print('In constructor!')
        self.name = name
        self.salary = salary
        Employee.count += 1

    def getEmployeeDetails(self):
        print("Employee Details: ")
        print("Name: ", self.name)
        print("Salary: ", self.salary)


emp1 = Employee("obb", 8888)
emp2 = Employee("kia", 4888)
emp3 = Employee("mz", 8488)
emp4 = Employee("yez", 8288)

emp1.getEmployeeDetails()
emp2.getEmployeeDetails()
emp3.getEmployeeDetails()
emp4.getEmployeeDetails()

print("Team Count: ", Employee.count)
print("Access instance attributes directly!")
print("emp1 is " +  emp1.name + " " + str(emp1.salary))