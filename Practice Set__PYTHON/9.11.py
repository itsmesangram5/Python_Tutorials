import os
with open('sample8.txt','r') as m:
   x=m.read()
with open ('renameSample8.txt','w') as m:
    m.write(x)
os.remove('sample8.txt')