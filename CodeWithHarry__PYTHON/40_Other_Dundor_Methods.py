class Number():
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("Lets Add   ")
        return self.num + num2.num
    def __mul__(self,num2):
        print("Lets Multiply  ")
        return self.num * num2.num
    def __str__(self):
        return f"Decimal Number  {self.num}"        #_______if you dont use this then output will be
                                                                           # <__main__.Number object at 0x000001AE39DE0FD0>
    def __len__(self):
        return 1                                                                      
    
n=Number(9)
print(n)    
print(len(n))