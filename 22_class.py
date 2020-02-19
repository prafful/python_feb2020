"""
1. class keyword
2. instance attributes!
3. class attributes
4. __init__ method -> constructor
5. self
"""

class Employee:
   
    count = 0
    def __init__(self):
        print("In constructor!")
        Employee.count += 1

    def getEmployeeCount(self):
        print("Employee Count: ")
        print(self.count)
        


emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.getEmployeeCount()
