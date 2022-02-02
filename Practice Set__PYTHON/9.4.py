with open('sample5.txt') as p:
   m=p.read()
   # for 'donkey' in m:
   #    #  if 'donkey' in line :
   #       p.write( m.replace( 'donkey', '#####'))
   #       print("Match Found")
   # else:
   #      print('Match Not Found!!')
   m=m.replace('donkey','@#$%^&')
with open('sample5.txt','w') as p:
   p.write(m)
    
