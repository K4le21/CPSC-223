prompt = "\nPlease enter pizza toppings: "
prompt += "\nEnter 'quit' to end the program. "

userInput = ""
pizzaList = []

while userInput != 'quit':
    userInput = input(prompt)
    pizzaList.append(userInput)
    print (userInput.title() + " was added to your pizza.")

pizzaList.remove("quit")
print (pizzaList)