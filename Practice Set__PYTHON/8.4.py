def sum(n):
    if n==0 or n==1:
        return n
    else:       
      return sum(n-1)+n
n=int(input("Enter the N\n"))
print(sum(n))