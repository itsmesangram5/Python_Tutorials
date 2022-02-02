n=int(input("Enter the valu of n \n "))
i=1
L=list()
while (i<n+1):
    i=i+1
    L.append(i)

print("The sum of first ",n," natural numbers is ",(sum(L)-n))

z=int(input("Enter the valu of n \n "))
i=1
p=1
while (i<z):
    p=p+(i+1)
    i=i+1
print("The sum of first ",z," natural numbers is ",p)  