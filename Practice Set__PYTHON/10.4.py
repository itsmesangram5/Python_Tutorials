import math
class calci():
    @staticmethod
    def greet():
        print("Hello__User ...your operations are    ")
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
s.greet()
s.square(a)  
s.cube()
s.squareroot()