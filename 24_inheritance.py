class Employee:

    def __init__(self, fname, lname):
        print("In Employee Constructor!")
        self.fname = fname
        self.lname = lname

    def getFname(self):
        return self.fname    

    def getLname(self):
        return self.lname   

    def getEmployeeDetails(self):
        print("In getEmployeeDetails of Employee!")      

class FullStackEngineer(Employee):     
    def __init__(self, fname, lname, tech):
        self.tech = tech
        super().__init__(fname, lname)     

    def getEmployeeDetails(self):    
        return "Name: " + self.fname + " " + self.lname + "\n" + "Technology: " + self.tech


fse1 = FullStackEngineer("O", "BB", "Java")
print(fse1.getEmployeeDetails())
print(fse1.getFname())
print(fse1.getLname())

emp1 = Employee("Yuko", "San")
emp1.getEmployeeDetails()

