import os.path
from os import path
counter = 0
user_input = input("Please input a word to search for: ")
try:
    with open("The call from beyond by Clifford D. Simak.txt", "r") as my_file:
        for line in my_file:
            split = line.split()
            for item in split:
                if item == user_input:
                    counter += 1

    print ("The word \'" + user_input + "\' appears " + str(counter) + " times.")

except FileNotFoundError:
    print ("File does not exist.")