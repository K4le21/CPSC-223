import json
filename = "populationbycountry.json"

with open(filename) as f:
    data = json.load(f)

print (data) 