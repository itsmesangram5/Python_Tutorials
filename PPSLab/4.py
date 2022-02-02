import math
a=input("Enter a number  ")
a=int(a)
print("Square root of no.is   ",math.sqrt(a))
print("Square of no. is  ",a*a)
print("Cube of no. is   ",a*a*a)
def createList(r1, r2):
    return [item for item in range(r1, r2-1)]
r1, r2 = 2,a
p=createList(r1, r2) 
L=[]
P=[]
for i in p :
  if(a%i!=0):
     L.append(1)
  else:
     P.append(2)
d=len(P) 
if d==0:
    print(a,"Is prime number")
else:
    print(a,"Is not prime number")

def fact(a):
    if a==0:
        return 1
    return a*fact(a-1)   
a=int(a)
print("Factorial of ",a," is ",fact(a))        