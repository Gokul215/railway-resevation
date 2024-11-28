from Passenger import Passenger 
# from Booker import Booker 
# from utils import Passenger
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
           
            Main.ractoticket(racpass)

class Main():
    def bookTicket(p):
        print(p.pid)
        # print(Booker.availableLowerBerths)
        if Booker.availableWaitinglist <1:
            print("NO tickets")
            return
        if p.pprefer=='L' and Booker.availableLowerBerths>0:
            print('Lower berth given')
            Booker.bookticket(p,Booker.lowerBerthsPositions[0],"L")
            Booker.lowerBerthsPositions.pop(0)
            Booker.availableLowerBerths-=1
            
        elif p.pprefer=='M' and Booker.availableMiddleBerths>0:
            print('Middle berth given')
            Booker.bookticket(p,Booker.middleBerthsPositions[0],"M")
            Booker.middleBerthsPositions.pop(0)
            Booker.availableMiddleBerths-=1
            
        elif p.pprefer=='U' and Booker.availableUpperBerths>0:
            print('Upper berth given')
            Booker.bookticket(p,Booker.upperBerthsPositions[0],"U")
            Booker.upperBerthsPositions.pop(0)
            Booker.availableUpperBerths-=1
            
            
        elif Booker.availableLowerBerths>0 and  p.pprefer!='L' :
            option=input("Lower berth available you want to book type yes or no: ")
            if option=='yes':
                print('Lower berth given')
                Booker.bookticket(p,Booker.lowerBerthsPositions[0],"L")
                Booker.lowerBerthsPositions.pop(0)
                Booker.availableLowerBerths-=1
            else:
                print("no booking")
                return
            
        elif Booker. availableMiddleBerths>0 and p.pprefer!='M' :
            option=input("Middle berth available you want to book type yes or no: ")
            if option=='yes':
                print('Middle berth given')
                Booker.bookticket(p,Booker.middleBerthsPositions[0],"M")
                Booker.middleBerthsPositions.pop(0)
                Booker.availableMiddleBerths-=1
            else:
                print("no booking")
                return
        elif Booker.availableUpperBerths>0 and p.pprefer!='U':
            option=input("Upper berth available you want to book type yes or no: ")
            if option=='yes':
                print('Upper berth given')
                Booker.bookticket(p,Booker.upperBerthsPositions[0],"U")
                Booker.upperBerthsPositions.pop(0)
                Booker.availableUpperBerths-=1
            else:
                print("no booking")
                return
            
        
        elif Booker.availableRacTickets>0:
            print("RAC given")
            Booker.bookractivket(p,Booker.racPositions[0],"RAC")
            Booker.racPositions.pop(0)
            Booker.availableRacTickets-=1
        elif Booker.availableWaitinglist>0:
            print('Waiting list given')
            Booker.bookwaitingticket(p,Booker.waitinglistPositions[0],"WL")
            Booker.waitinglistPositions.pop(0)
            Booker.availableWaitinglist-=1
    def cancelTicket(id):
        if id in Booker.Passengers:
            Booker.cancelticket(id)
            print('Ticket cancelled successfully')
        else:
            print('Invalid passenger id')
    def ractoticket(p):
         if Booker.availableLowerBerths>0  :
                print('Lower berth given')
                Booker.bookticket(p,Booker.lowerBerthsPositions[0],"L")
                Booker.lowerBerthsPositions.pop(0)
                Booker.availableLowerBerths-=1
            
         elif Booker.availableMiddleBerths>0  :
                print('Middle berth given')
                Booker.bookticket(p,Booker.middleBerthsPositions[0],"M")
                Booker.middleBerthsPositions.pop(0)
                Booker.availableMiddleBerths-=1
        
         elif Booker.availableUpperBerths>0 and p.pprefer!='U':
                print('Upper berth given')
                Booker.bookticket(p,Booker.upperBerthsPositions[0],"U")
                Booker.upperBerthsPositions.pop(0)
                Booker.availableUpperBerths-=1
           

while True:
    print(" 1. Book ticket \n 2. Cancel ticket \n 3. Available tickets \n 4. Booked tickets \n 5. Exit")
    choice=int(input('Enter your choice: '))
    print("----------------------")
    
    match choice:
        case 1:
            name=input("Enter your name: ")
            age=int(input("Enter your age: "))
            preference=input("Enter your preference (l or u or m): ").upper()
            p=Passenger(name,age,preference)
            Main.bookTicket(p)
            
        case 2:
            id=int(input('Enter the passenger id: '))
            Main.cancelTicket(id)
             
        case 3:
            # booker=Booker()
            print("Available Lower berth:",Booker.availableLowerBerths)
            print("Available Upper berth:",Booker.availableUpperBerths)
            print("Available Middle berth:",Booker.availableMiddleBerths)
            print("Available rac list:",Booker.availableRacTickets)
            print("Available waiting list:",Booker.availableWaitinglist)
            print("----------------------")
        case 4:
        #    booker=Booker()
           if not Booker.Passengers:
             print('No passengers')
           else:
                for i in Booker.Passengers.values():
                    print('----------------------')
                    print("Passenger id: ",i.pid)
                    print("Passenger name: ",i.pname)
                    print("Passenger age: ",i.page)
                    print("Passenger status: ",str(i.seatnumber)+str(i.alloted))
                    print('----------------------')
            
        case _:
            break


