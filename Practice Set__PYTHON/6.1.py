a=int(input("Enter a Number \n  "))
b=int(input("Enter a Number \n  "))
c=int(input("Enter a Number \n"))
d=int(input("Enter a Number  \n"))
L=[a,b,c,d]
if(a>b and a>c and a>d):
    print(a,"  Is maximum")
elif(b>a and b>c and b>d):
     print(b,"  Is maximum")   
elif(c>b and c>a and c>d):
    print(c,"  Is maximum")  
else:
    print(d,"  Is maximum")    