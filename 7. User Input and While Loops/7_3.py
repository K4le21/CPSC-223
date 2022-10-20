userInput = input("Please enter a number: ")

userInput = int(userInput)

if userInput % 10 == 0:
    print (str(userInput) + " is a mutiple of 10.")
else:
    print (str(userInput) + " is not a mutiple of 10.")