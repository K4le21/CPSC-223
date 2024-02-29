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
    if not os.path.isfile(filename_one):
        print(filename_one + ' does not exist.')
    if not os.path.isfile(filename_two):
        print(filename_two + ' does not exist.')