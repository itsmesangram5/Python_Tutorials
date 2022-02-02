num = int(input("Enter a number: "))  
if num > 1:  
   for i in range(2,num):        
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  


#My logic


# a=input("Enter a number  ")
# a=int(a)
# def createList(r1, r2):
#     return [item for item in range(r1, r2-1)]
# r1, r2 = 2,a
# p=createList(r1, r2) 
# L=[]
# P=[]
# for i in p :
#   if(a%i!=0):
#      L.append(1)
#   else:
#      P.append(2)
# d=len(P) 
# if d==0:
#     print(a,"Is prime number")
# else:
#     print(a,"Is not prime number")