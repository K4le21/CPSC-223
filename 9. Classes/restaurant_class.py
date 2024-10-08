class Restaurant:
    def __init__(self, restraunt_name, cuisine_type, number_served = 0):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self):
        self.number_served += 1

    def describe_restaurant(self):
        print (self.restraunt_name + " " + self.cuisine_type + " " + str(self.number_served))
    
    def open_restaurant(self):
        print (self.restraunt_name + " is now open and serves " + self.cuisine_type + " food.")