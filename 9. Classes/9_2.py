class Restaurant:
    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print (self.restraunt_name + " " + self.cuisine_type)
    
    def open_restaurant(self):
        print (self.restraunt_name + " is now open and serves " + self.cuisine_type + " food.")

restraunt1 = Restaurant("Joe's Crab Shack", "Seafood")
restraunt2 = Restaurant("Moe's Burger", "American")
restraunt3 = Restaurant("Lucky Panda", "Chinese")


restraunt1.describe_restaurant()
restraunt1.open_restaurant()

restraunt2.describe_restaurant()
restraunt2.open_restaurant()

restraunt3.describe_restaurant()
restraunt3.open_restaurant()