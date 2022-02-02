# list_of_marks=[ ] wrong way
# use int function for marks
a=int(input("Enter 1st student Marks\n"))
b=int(input("2nd\n"))
c=int(input("3rd\n"))
d=int(input("4th\n"))
e=int(input("5th\n"))
f=int(input("6th\n"))
# list_of_marks.insert(0,a)
# list_of_marks.insert(1,b)
# list_of_marks.insert(2,c)
# list_of_marks.insert(3,d)
# list_of_marks.insert(4,e)
# list_of_marks.insert(5,f) wrong Way
list_of_marks=[a,b,c,d,e,f]
list_of_marks.sort()
print(list_of_marks)