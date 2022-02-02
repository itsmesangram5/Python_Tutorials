class RailwayForm:
    formtype="RailwayReservation"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Name is {self.train}")

harryaplication=RailwayForm()
harryaplication.name='Sangram'
harryaplication.train='RajdhaniExpress'
harryaplication.printdata()