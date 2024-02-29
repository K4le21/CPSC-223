user_input = input("What is your name? ")

file1 = open("guest.txt", "w")
file1.write(user_input)
file1.close()

file1 = open('guest.txt', 'r')
print(file1.read())
file1.close()