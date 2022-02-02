class a:
    def h(self):
        print(" Class A")
class b(a):
    def h(self):
        print(" Class B")
class c(b):
    def h(self):
        print(" Class C")   
class g(a):
    def h(self):
        super().h()
        print("Class G") 
z=g()

z.h()
#______Use of superclass is to call the base class  and also run its method