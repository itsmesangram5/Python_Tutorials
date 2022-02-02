class Employee:
    salary=500
    increment=5
    @property
    def salafterinc(self):
        return self.salary+self.increment
    @salafterinc.setter
    def salafterinc(self):
        (self.salary)*(1/100)=(self.increment)
s=Employee()
print(s.salafterinc)
s.salafterinc=1000
print(s.increment)
print(s.salary)
