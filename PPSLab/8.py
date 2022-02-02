try:
 fin = open("input.txt",'r')   
 fout = open("output.txt",'w') 

 for line in fin:
  line = line.swapcase()   #Replace lower case with upper and upper with lower
  line = line.replace(".","*")  
  fout.write(line)
except:
 print("File error occured")