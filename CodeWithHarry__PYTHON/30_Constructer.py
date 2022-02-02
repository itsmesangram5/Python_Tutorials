class Employee():
    company="Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("This is printed without running the function")

    def getdetails(self):
        print(f"Name of the Employee is {self.name}")   
        print(f"Salary of the Employee is {self.salary}") 
        print(f"Subunit of the Employee is {self.subunit}")  
        
    def getsalary(self,sign):
        print(f"Salary is {self.salary} working in {self.company}\n{sign} ")

    @staticmethod
    def greet():
        print("Good Morning")


harry=Employee("Sangram",500,"Gmail")   
harry.getdetails()  
harry.getsalary("Ohhk")                   #this will autometically take inputs given to employee______this only happens if there is init 
                                                                      #function present there

# harry.salary=100
# harry.getsalary("Thanks")        #==Employee.getsalary(harry)
# harry.greet()
#######_____________Self parameter is autometically passed through the function_______________________
