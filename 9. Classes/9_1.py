class Restaurant:
    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print (self.restraunt_name + " " + self.cuisine_type)
    
    def open_restaurant(self):
        print (self.restraunt_name + " is now open and serves " + self.cuisine_type + " food.")

new_Restaurant = Restaurant("Joe's Crab Shack", "Seafood")

new_Restaurant.describe_restaurant()
new_Restaurant.open_restaurant()