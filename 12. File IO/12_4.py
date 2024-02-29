print ("Enter 'quit' to quit.")
user_input = input("What is your name? ")
file1 = open("guest_book.txt", "w")

while user_input != "quit":
    print("Welcome " + user_input + "!")
    file1.write(user_input + "\n")
    user_input = input("What is your name? ")


file1 = open("guest_book.txt", "r")
print(file1.read())
file1.close()