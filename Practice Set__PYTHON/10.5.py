seatlist=[]
class train():
    formtype="Indian Railways"
    def __init__(self,ntrain,fair):
        self.ntrain=ntrain
        self.fair=fair
        m=0
        while self.ntrain>=m:
            seatlist.append(m)
            m=m+1 

    def get_status(self):
        print(f"There are {seatlist} seats now")
    def get_fair_imfo(self):
        print(f"The fair for each train is Rs. {self.fair}")
    def book_ticket(self,number):
        if number in seatlist:
          print(f"you can book the seats___Your seat no. is {number} If you want to book ticket please visit the website") 
          seatlist.remove(number)
        else:
            print("Sorry this seat is not available now ...!!")  
    def cancelticket(self,number):
        if number in seatlist:
            print("Sorry This seat is not booked yet")
        else:    
            seatlist.append(number)              
sangram=train(10,500)
sangram.get_fair_imfo()
# y=input("Enter the Tickt no. you want to book  ") 
sangram.book_ticket(11)
sangram.book_ticket(9)
sangram.get_status()  
# sangram.cancelticket(9)  
# sangram.get_status() 
sangram.book_ticket(9)
