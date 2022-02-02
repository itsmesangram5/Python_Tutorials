n=int(input("Enter the n   "))
for  i in range(-1,n+1):
    print(" "*(n-i),"*"*((n*i)-i-1)," "*(n-i))
    