from case9_4 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    
    def display_flavors(self,):
        print(f"{self.flavors} is the best of all time for me")