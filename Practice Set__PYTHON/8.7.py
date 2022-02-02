def createlist(a,b):
   return [ item for item in range(a,b) ]
e=input("Do you want to create ypur own list \n if yes typr yes if not enter no  ")
if e=="yes" or "YES" :
    a,b=int(input("Enter starting   ")),int(input("Enter end   "))  
elif (e=="no" or "NO"):
    a,b=1,5
d=createlist(a,b)
print(d)
def wremove(z):
    return(d.remove(z))
z=int(input("Enter item which you want to remove "))
y=wremove(z)
print(y)           