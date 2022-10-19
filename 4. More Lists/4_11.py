pizzaList = ["pepperoni pizza", "margherita pizza", "BBQ Chicken Pizza"]
friend_pizza = pizzaList.copy()
friend_pizza.append("Buffalo Pizza")

print("My favorite pizzas are: ")
for x in pizzaList:
    print(x)

print ("My friend's favorite pizzas are: ")
for x in friend_pizza:
    print(x)