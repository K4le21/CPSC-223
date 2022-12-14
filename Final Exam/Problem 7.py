import json

numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0]
filename = "populationbycountry.json"

with open(filename) as f:
    data = json.load(f)

for key in data:
    population = str(key['population'])
    leadingNum = population[0]
    if not leadingNum == '0':
        index = numList.index(leadingNum)
        frequency[index] += 1

print (frequency)