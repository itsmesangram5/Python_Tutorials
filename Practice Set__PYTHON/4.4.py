# n[]  dont write list first 
# write it after taking input
a=int(input("Enter 1st Number\n"))
b=int(input("2nd\n"))
c=int(input("3rd\n"))
d=int(input("4th\n"))
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)  use int direct 
# n.insert(0,a)
# n.insert(1,b)
# n.insert(2,c)
# n.insert(3,d)
n=[a,b,c,d]
print(" The list is " ,n)
# z=a+b+c+d
# z=int(z) 
# print("The sum of No. in list is",z)
# Another way to sum a list
print("The sum of No. in list is",n[0]+n[1]+n[2]+n[3])
print(sum(n))
# using sum function 