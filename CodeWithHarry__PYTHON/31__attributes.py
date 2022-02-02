class Employee():
    company="Google"     #_______________Class attribute
    def getsalary(self,salary,company,sign):
        print(f"Salary is {salary} working in {company}\n{sign} ")

    def argument(self,z):
         print(f"This is employee age is {self.z}") 



         

harry=Employee()                #==Employee.getsalary(harry)
# harry.company="Youtube"     # ___________Instance attribute           
# harry.salary=100
# harry.sign="Ohhhk"
harry.getsalary(100,"IBM","Good")         #______you can also write like this
harry.z=10      