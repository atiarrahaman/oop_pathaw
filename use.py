from abc import ABC,abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self,name,phone,email) -> None:
        self.name=name 
        self.phone=phone 
        self.email=email 
    
    @abstractmethod
    def Display_profile(self):
        print("my_profile ")


class Rider(User):
    def __init__(self, name, phone, email,current_location,inisial_balance) -> None:
        self.current_location=current_location
        self.wallet=inisial_balance
        self.current_ride=None

        super().__init__(name, phone, email)

    def Display_profile(self):
        print("rider profile")
    
    def Load_balance(self,amount):
        if amount > 0:
            self.wallet += amount

    def Update_location(self,current_location):
        self.current_location=current_location


    def Ride_Request(self,destination):
        if not self.current_ride:
            ride_request=Request_ride(self,destination)
            ride_macher=Ride_macthiing()
            self.current_ride=ride_macher.Find_driver(ride_request)



class Driver(User):
    def __init__(self, name, phone, email,nid,licens_nmb,wallet) -> None:
        self.__nid=nid
        self.licens_nmb=licens_nmb
        self.wallet=wallet
        super().__init__(name, phone, email)


    def Display_profile(self):
        print('driver profile')

    def Accept_ride(self,ride,):
        ride.set_driver(self)


class Ride():
    def __init__(self,current_locatiion,destination,fare) -> None:
        self.current_location=current_locatiion
        self.destination =destination
        self.driver=None
        self.rider=None
        self.fare=fare
        self.start_time=None
        self.end_time=None

    def set_driver(self,driver):
        self.driver=driver

    def Start_ride(self):
        self.star_ride=datetime.now()

    def End_ride(self):
        self.end_ride=datetime.now()



class Request_ride():
    def __init__(self,rider,destination) -> None:
        
        self.destination=destination
        self.rider=rider


class Ride_macthiing():
    def __init__(self) -> None:
        self.drivers=[]

    
    def Find_driver(self,request_ride):
        if self.drivers > 0:
            driver=self.drivers[0]
            ride=Ride(request_ride.rider.current_locatiion,request_ride.destination)
            driver.Accept_ride(ride)
            return ride

    










roc=Rider('roc',87878,'a@a.com','motijiil',80)
roc.Load_balance(100)
print(roc.wallet)