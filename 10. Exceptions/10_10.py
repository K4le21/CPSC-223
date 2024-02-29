import os.path
from os import path
counter = 0
try:
    with open("The call from beyond by Clifford D. Simak.txt", "r") as my_file:
        for line in my_file:
            split = line.split()
            for item in split:
                if item == "the":
                    counter += 1

    print ("The word 'the' appears " + str(counter) + " times.")

except FileNotFoundError:
    print ("File does not exist.")