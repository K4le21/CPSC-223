print ("Enter two numbers to be added.")
numOne = input("Enter your first number: ")
numTwo = input("Enter your second number: ")

try:
    numOne = float(numOne)
    numTwo = float(numTwo)

    print(numOne + numTwo)
except ValueError:
    print("The provided value entered was not a number.")