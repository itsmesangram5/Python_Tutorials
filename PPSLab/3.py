class Student:    
 def __init__(self): 
  self.marks = []
  self.passed = True

 def input(self):  
          
  try:
   for i in range(5):
    mark = float(input("Enter Marks "))
    self.marks.append(mark)
    if mark < 40:
     self.passed = False
  except:
   print("Enter marks in digits.")

 def grade(self):  
     
  if self.passed:
   average = sum(self.marks)/5
   print(" Your aggregate is ",average)
   if average>75:
    print("Distinction")
   elif average >= 60 and 75> average:
    print("First Division")
   elif average >= 50 and 60> average:
    print("Second Division")
   else: 
    print("Third Division")
  else:
   print("Failed")   

if __name__ == '__main__':
 student = Student()
 student.input()   
 student.grade()