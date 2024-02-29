import json

user_input = input("What is your favorite number? ")
write_input = json.dumps(str(user_input))
open("favoriteNumber.json","w").write(write_input)