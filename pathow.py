from abc import ABC ,abstractmethod
from datetime import datetime

class Ride_sharing():
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.drivers=[]
        self.riders=[]
        self.ride=[]
    

    def Add_Drivers(self,driver):
        self.drivers.append(driver)

    def Add_Riders(self,rider):
        self.riders.append(rider)
        

    def __repr__(self) -> str:
        return f'drivers: {self.drivers} and Riders: {self.riders}'




class User(ABC):
    def __init__(self,name,phone,email) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        
        
    @abstractmethod
    def Dispaly_profile(self):
        print("my Profile")

class Rider(User):
    def __init__(self, name, phone, email,current_location) -> None:
        self.current_ride=None
        self.current_location=current_location
        self.wallet=0
        super().__init__(name, phone, email, )


    def update_location(self,current_location):
        self.current_location=current_location

    def Dispaly_profile(self):
        print("client Profile")
    


    def request_ride(self,destination):
        if not self.current_ride:
            #todo 
            ride_request=Ride_Reuest(self,destination)
            ride_mather=Ride_Macthing()
            self.current_ride=ride_mather.find_drivers(ride_request)

    def Load_amount(self,amount):
        if amount > 0:
            self.wallet +=amount
    
class Driver(User):
    def __init__(self, name, phone, email,nid,car_number) -> None:
        self.__nid=nid
        self.carNumber=car_number
        self.wallet=0
        super().__init__(name, phone, email)

    def Dispaly_profile(self):
        print("driver profile")


    def accept_ride(self,ride):
        ride.set_driver(self)


class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.fare=0

    def set_driver(self,driver):
        self.driver=driver


    def start_ride(self):
        self.start_time=datetime.now()

    def End_ride(self):
        self.end_time=datetime.now()
        self.clinet.wallet -= self.fare
        self.driver.wallet +=self.fare


class Ride_Reuest():
    def __init__(self,rider,end_location) -> None:
        self.rider=rider
        self.end_location=end_location


class Ride_Macthing():
    def __init__(self) -> None:
        self.drivers=[]

    def find_drivers(self,ride_request):
        if self.drivers > 0 :

            #todo
            driver=self.drivers[0]
            ride=Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_ride(ride)

            return ride



class Vehical(ABC):
    def __init__(self,licens_plate,vehical_type,rate) -> None:
        self.licens_plate=licens_plate
        self.vehical_type=vehical_type
        self.rate=rate

    @abstractmethod
    def Start_drive(self):
        self.status='available'


class Car(Vehical):
    def __init__(self, licens_plate, vehical_type, rate,model) -> None:
        self.model=model
        super().__init__(licens_plate, vehical_type, rate)
    

    def Start_drive(self):
        self.status='ubavailable'
    


class Bike(Vehical):

    def __init__(self, licens_plate, vehical_type, rate,model,cc) -> None:
        self.model=model
        self.cc=cc
        super().__init__(licens_plate, vehical_type, rate)
    
    def Start_drive(self):
        self.status='unavailable'



pathw=Ride_sharing('pathaw')

nijam=Rider('nijam', 88908,'jin@nn.com','utoora')


ajim=Driver('ajim',7774,'aaa@.com',7676,878)

print(ajim.name)