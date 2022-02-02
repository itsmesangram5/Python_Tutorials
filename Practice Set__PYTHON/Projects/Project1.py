import random
def game(comp,b):
    if comp==b:
        return None
    elif comp=="s":
        if b=="W":
            return False
        elif b=="g":
            return True
    elif comp=="w":
        if b=="W":
            return False
        elif b=="g":
            return True        


    
print("Comp Turn : Snake(s) Water(w) or Gun(g)")
randNo= random.randint(1,3)
if randNo==1:
    comp="s"
elif randNo==3:
    comp="w"
elif randNo==3:
    comp="g"

b=input("Players Turn : Snake(s) Water(w) or Gun(g)")
game(comp,b)         