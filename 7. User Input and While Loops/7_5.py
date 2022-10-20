userInput = input("How old are you? ")

userInput = int(userInput)

if userInput > 12:
    print ("Your ticket is $15.")
elif userInput > 3 and userInput < 12:
    print ("Your ticket is $10.")
else:
    print ("Your ticket is free.")