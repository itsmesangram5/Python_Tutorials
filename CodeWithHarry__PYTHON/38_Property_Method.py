class Employee :
    company="Dell"
    name="Sangram"
    salary=1000
    bonus=500
    @property
    def totalsalary(self):
        return self.salary + self.bonus  

    @totalsalary.setter 
    def totalsalary(self,val):
        self.salary=val-self.bonus   

s=Employee()      
print(s.totalsalary)     #_____You can use it like a class atttribute not like a function
s.totalsalary=2000
print(s.salary)
print(s.bonus)
print(s.totalsalary)
print(Employee.salary)