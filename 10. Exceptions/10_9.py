import os.path
from os import path

try:
    cats = open("cats.txt", "r")
    dogs = open("dogs.txt", "r")

    print(cats.read())
    print(dogs.read())
    cats.close()
    dogs.close()
except FileNotFoundError:
    filename_one = "cats.txt"
    filename_two = "dogs.txt"
    if os.path.isfile(filename_one):
        with open(filename_one, 'r') as f:
            print(f.read())
    else:
        print(filename_one + ' does not exist.')
    if os.path.isfile(filename_two):
        with open(filename_two, 'r') as f:
            print(f.read())
    else:
        print(filename_two + ' does not exist.')