class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometr(self):
        print(f"This car {self.odometr_reading} miles on it")
        
    def update_odometr(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometr")
            
    def incremetn_odometr(self, miles):
        self.odometr_reading += miles
        

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")
        
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full cahrge")
        
    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65
        
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
        
teslacxy = ElectricCar("xcv", "delte", 1978)
teslacxy.battery.get_range()
teslacxy.battery.upgrade_battery()
teslacxy.battery.get_range()