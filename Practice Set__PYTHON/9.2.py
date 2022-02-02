p=open('sample3.txt','r')
q=(p.read())
a=int(input("Enter your score   ")) 
if q=='':
    m=str(a)
    with open('sample3.txt','w') as f :
     f.write(m)
    print("New high score is  ",a)
elif a>(int(q))  :
    m=str(a)
    with open('sample3.txt','w') as f :
     f.write(m)
    print("New high score is  ",a)
else:
    print("You Lost!!    High Score is ",q)        
p.close()