print ("Enter 'quit' to quit.")
user_input = input("Why do you like programming?\n")
file1 = open("reasons.txt", "w")

while user_input != "quit":
    file1.write(user_input + "\n")
    user_input = input("Why do you like programming?\n")


file1 = open("reasons.txt", "r")
print(file1.read())
file1.close()