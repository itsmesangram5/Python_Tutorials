with open('sample6.txt','r') as p:
   m=p.read().lower()
   if 'python' in m :
     print("Match Found")
   else:
     print('Match Not Found!!')
    
