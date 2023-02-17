class train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("********")
        print(f"the name of train is {self.name}")
        print(f"the seats available in the train are {self.seats}")

    def fareInfo(self):
        print("******")
        print(f"the price of the train ticket is RS{self.fare}")

    def bookTIcket(self):
        print("****")
        if(self.seats>0):
            print(f"your ticket has been booked ! Your seat No is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full !kindly try in tatkal")
    def cancleTicket(self):
        pass 


intercity = train("intercity exprees : 145634",90,1)
intercity.getStatus()
intercity.bookTIcket()

intercity.getStatus()
intercity.bookTIcket()
