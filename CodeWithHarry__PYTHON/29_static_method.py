class Employee():
    company="Google"
    def getsalary(self):
        print(f"Salary is {self.salary} working in {self.company}\n{self.sign} ")

    def argument(self,z):
         print(f"This is employee age is {self.z}")   

    @staticmethod
    def greet():
        print("Good Morning")


harry=Employee()                #==Employee.getsalary(harry)
harry.company="Youtube"     # ___________Instance attribute           
harry.salary=100
harry.sign="Ohhhk"
harry.getsalary()
harry.z=10           # hare it will take z=10 preference to instance attribute
harry.argument(999)      #hence output will be____________ This is employee age is 10
harry.greet()

