class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}. It is {self.type} type cuisine")
        
    def open_restaurant(self):
        print("The restaurant is open")
        
    def set_number_served(self, customers):
        self.served = customers
        
    def increment_servers(self, increment):
        self.served += increment

restaurant = Restaurant("TTZ gumma", "studentiskiy")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# print(restaurant.served)

# restaurant.served = 28

# print(restaurant.served)

restaurant.set_number_served(378)
print(restaurant.served)

restaurant.increment_servers(1203)
print(restaurant.served)