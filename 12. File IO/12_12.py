import json


with open('favoriteNumber.json') as f:
    lines = f.readline()
lines = lines.replace('"','')

user_input = input("What is your favorite number? ")
if user_input == lines:
    print("Your favorite number is " + lines + ".")
else:
    write_input = json.dumps(str(user_input))
    open("favoriteNumber.json","w").write(write_input)
    with open('favoriteNumber.json') as f:
        lines = f.readline()
        print("I know your favorite number! It's " + lines + ".")