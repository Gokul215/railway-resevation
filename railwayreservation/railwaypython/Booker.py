from collections import deque
class Booker():
    availableLowerBerths=1
    availableMiddleBerths =1
    availableUpperBerths =1
    availableRacTickets=1
    availableWaitinglist=1
    
    waitinglist=deque()
    raclist=deque()
    
    lowerBerthsPositions=[1]
    upperBerthsPositions=[1]
    middleBerthsPositions=[1]
    racPositions=[1]
    waitinglistPositions=[1]
    
    Passengers={}
    
    def bookticket(p,seatnumber,alloted):
        p.seatnumber=seatnumber
        p.alloted=alloted
        Booker.Passengers[p.pid]=p
        print("Booked successfully......")
        
    def bookractivket(p,seatnumber,alloted):
        p.seatnumber=seatnumber
        p.alloted=alloted
        Booker.Passengers[p.pid]=p
        Booker.raclist.append(p)
        print("RAC added successfully......")
        
    def bookwaitingticket(p,seatnumber,alloted):
        p.seatnumber=seatnumber
        p.alloted=alloted
        Booker.Passengers[p.pid]=p
        Booker.waitinglist.append(p)
        print("WL added successfully......")
    
    def cancelticket(id):
        p=Booker.Passengers[id]
        del Booker.Passengers[id]
        if p.alloted=="L":
            Booker.availableLowerBerths+=1
            Booker.lowerBerthsPositions.append(p.seatnumber)
        elif p.alloted=="M":
            Booker.availableMiddleBerths+=1
            Booker.middleBerthsPositions.append(p.seatnumber)
        elif p.alloted=='U':
            Booker.availableUpperBerths+=1
            Booker.upperBerthsPositions.append(p.seatnumber)
        
        if len(Booker.raclist)>0:
            racpass=Booker.raclist.popleft()
            racpassseat=racpass.seatnumber
            Booker.racPositions.append(racpassseat)
            Booker.availableRacTickets+=1
            
            if len(Booker.waitinglist)>0:
                wlpass=Booker.waitinglist.popleft()
                wlpassseat=wlpass.seatnumber
                Booker.waitinglistPositions.append(wlpassseat)
                Booker.availableWaitinglist+=1
                
                wlpass.seatnumber=Booker.racPositions[0]
                wlpass.alloted="RAC"
                Booker.racPositions.pop(0)
                Booker.raclist.append(wlpass)
                
                Booker.availableRacTickets-=1
            # from Main import Main
           
            Main.bookTicket(racpass)
            
    

            
    
    
    
    

    
    
    