# NAME=input("Enter Name")
# DATE=input("Enter Date")
# letter="Dear \n"+ NAME +" ,You  are Selected !\n"+ DATE
# print(letter)
# print(letter.count("  "))
# print(letter.replace("  "," "))
# this is also correct but according to que its ans should be fidd
letter=''' Dear <|NAME|>  
                    You Are Selected !
      Date <|DATE|>'''
a=input("Enter Your name \n")  
b=input("Enter the Date\n")   
c= letter.replace("<|NAME|>",a)
c= c.replace("<|DATE|>",b)
print(c)
# This program is using replace functio