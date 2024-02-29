import json

with open('favoriteNumber.json') as f:
    lines = f.readlines()
    print("I know your favorite number! It's " + str(lines) + ".")

