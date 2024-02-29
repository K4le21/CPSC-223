from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

dice1 = Die()

dice2 = Die(10)

dice3 = Die(20)


for i in range(1,10):
    dice1.roll_die()
    dice2.roll_die()
    dice3.roll_die()
