class a:
    def __init__(self):
        print("Initializing person.....\n")


    def h(self):
        print(" Class A")


class b(a):
    def __init__(self):
        super().__init__()
        print("Initializing person.....and\n")

    def h(self):
        print(" Class B")
class c(b):
    def __init__(self):
        super().__init__()
        print("Initializing person.....and kill him\n")
    def h(self):
        print(" Class C")   
# class g(a,b,c):
#     def h(self):
#         super().h()
#         print("Class G") 
z=c()
# z.h()

#______Use of superclass is to call the base class  and also run its method