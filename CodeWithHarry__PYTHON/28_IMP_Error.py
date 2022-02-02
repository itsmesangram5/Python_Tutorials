class Employee():
    company="Google"
    def getsalary(self):
        print("Salary is 100k ")

harry=Employee()
harry.getsalary()        #==Employee.getsalary(harry)here one positional argument
# TypeError: getsalary() takes 0 positional arguments but 1 was given
# if you run above program without self argument then above error will show