m=True
i=1
with open('sample6.txt','r') as p:
   while m :
    m=p.readline()
    if 'python' in m.lower():
     print("Match Found")
     print(m)
     print("It is present in ",i)
    else:
     pass
    i=i+1
    

#     def findline(word):
#        for i in range(len(m)):
#           if word in m[i]:
#              print(i+1, end=", ")
# findline('python')            
