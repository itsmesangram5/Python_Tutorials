class Employee :
    company="Dell"
    name="Sangram"
    salary=100
     
    def changesalary(self,sal):
        self.salary=sal 
        

s=Employee()
print(s.salary)
z=s.changesalary(599)     
print(s.salary)    
print(Employee.salary)
# ___________Changes salary for that particular object not or the original classs
# __________If you wan to chage class attribute then you can use following
'''
class Employee :
    company="Dell"
    name="Sangram"
    salary=100
     
    def changesalary(self,sal):
        self.__class__.salary=sal 
'''        
#______OR the another way to change it is
'''
class Employee :
    company="Dell"
    name="Sangram"
    salary=100
    @classmethods
    def changesalary(sls,sal):
        sls.salary=sal 
'''        