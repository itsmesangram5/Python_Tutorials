n=int(input("Enter n\n") ) 
def createList(r1, r2):
     return [item for item in range(r1, r2+1)]
p=createList(0,n)
q=reversed(p)
def star(n):
   for i in q:
     print("*"*i)    
star(n)     
# or
# for i in range(n):
#      print("*"*(n-i))