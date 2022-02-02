n=int(input("Enter the value N \n"))
p=range(1,n-1)
q=range(1,n+1)
for i in q:
    print("* ",end="")
    if n-i in p:
        print("  "*(n-2),end="")
    else:
        print("* "*(n-2),end="")    
    print("* ")    