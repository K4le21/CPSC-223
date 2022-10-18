names = ["Elon Musk", "Kanye West", "Keanu Reeves", "Will Smith"]
print("My dinning table only has space for 2 guests.")

while (len(names) != 2):
    print("Sorry, " + names[len(names)-1] + " is no longer invited to the dinner.")
    names.pop()

for x in names:
    print(x + ", you are invited to my dinner.")

names.remove("Kanye West")
del names[0]

for x in names:
    print(x)