import math
class calci():
    def __init__(self,a):
        self.a=a 
    def square(self,a):
       print(a*a)
    def cube(self):
       print(self.a*self.a*self.a)
    def squareroot(self):
       print(math.sqrt(self.a))
a=input("Enter the Nummber ")
a=int(a)
s=calci(a)
s.square(a)  
s.cube()
s.squareroot()