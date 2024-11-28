class Passenger():
    id=1
   
    def __init__(self,name,age,prefer):
        # print(Passenger.id)
        self.pname=name
        self.page=age 
        self.pprefer=prefer
        self.pid=Passenger.id
        Passenger.id+=1
        self.alloted=''
        self.seatnumber=-1