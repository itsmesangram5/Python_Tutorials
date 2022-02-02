list=['donkey','he']

with open('sample5.txt') as p:
   m=p.read()
   for word in list:
    m=m.replace(word,'@#$%^&')
with open('sample5.txt','w') as p:
   p.write(m)
    
