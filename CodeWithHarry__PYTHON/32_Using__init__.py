class Employee():
    company="Google"     #_______________Class attribute
    def __init__(self,salary,company,sign):              #___________init__is used to assign the values to the whole class
        self.salary=salary
        self.company=company
        self.sign=sign
        print("ok")                     
        

    def getsalary(self):           #if you dont wont to write in () you have to use self.*****
        print(f"Salary is {self.salary} working in {self.company}\n{self.sign} ")

    def argument(self,z):
         print(f"This is employee age is {z}") #____argument defined in () called as positional argument

harry=Employee(100,"IBM","Good")#__This is also instance attribute                #==Employee.getsalary(harry)
harry.sign="new sign"     #instance attribute taking preference over class attribute
harry.getsalary()  
harry.argument(100)        
        #__If you are using init operator the you can directaly pass values through the Employee ie.class

#_____________________________________________________________________________________________________________________________#  
# class Employee():
#     company="Google"
#     def getsalary(self):
#         print(f"Salary is {self.salary} working in {self.company}\n{self.sign} ")

#     def argument(self,z):
#          print(f"This is employee age is {self.z}")   

#     @staticmethod
#     def greet():
#         print("Good Morning")


# harry=Employee()                #==Employee.getsalary(harry)
# harry.company="Youtube"     # ___________Instance attribute           
# harry.salary=100
# harry.sign="Ohhhk"
# harry.getsalary()
# harry.z=10           # hare it will take z=10 preference to instance attribute
# harry.argument(999)      #hence output will be____________ This is employee age is 10
# harry.greet()
      