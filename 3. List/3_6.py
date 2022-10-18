names = ["Elon Musk", "Kanye West", "Keanu Reeves", "Will Smith"]
names[3] = "Tom Hanks"
for x in names:
    print(x + ", you are invited to my dinner.")

print("Will Smith cannot make the dinner.")
print("I have found a larger dining table.")

names.insert(0, "Rick Astley")
names.insert(2, "Michael Jackson")
names.append("Mark Zuckerberg")

for x in names:
    print(x + ", you are invited to my dinner.")