class Employee():
    company="Google"     #_______________Class attribute
    def getsalary(self,salary,sign):
        print(f"Salary is {salary} working in {self.company}\n{sign} ")

class programer(Employee):        
    def argument(self):
         print(f"This is employee age is {self.z}") 
 
p=programer()
p.getsalary(100,"Good")
# e=Employee()
# e.argument()
