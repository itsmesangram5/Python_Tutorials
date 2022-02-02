def greatestno(a,b,c):
    if a>b and a>c:
        print(a," Is the greatest")
    elif b>a and b>c:
        print(b," Is the greatest")
    else :
        print(c," Is the greatest")
a=int(input("Enter first no.\n"))        
b=int(input("Enter second no.\n"))        
c=int(input("Enter third no.\n"))        
p=greatestno(a,b,c)