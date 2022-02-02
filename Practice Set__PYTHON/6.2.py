a=int(input("Enter Marks of 1st Subject \n"))
b=int(input("Enter Marks of 2st Subject \n"))
c=int(input("Enter Marks of 3st Subject \n"))
if((a or b or c)<33):
    print("Studant is fail")
elif(((a+b+c)/3)>40):
    print("Student is pass") 
else:
    print("Student is fail")    

            