a=int(input("Enter a Number\n"))
for i in range(2,a):
    if a%i==0:
        print(a,"  is not prime number")
        break
else:
    print(a,"  is prime number")    
