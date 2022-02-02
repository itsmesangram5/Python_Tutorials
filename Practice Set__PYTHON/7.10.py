a=int(input("Enter a Number\n"))
# p=[10,9,8,7,6,5,4,3,2,1]
def createList(r1, r2):
   return [item for item in range(r1, r2)]
q=createList(1,11)
p=reversed(q)
for i in p:
    print(f"{a}X{i}={a*i}")

