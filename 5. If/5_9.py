userList = ["Will", "Jaden", "admin", "Ryan", "Alex"]
userList.clear()
if not userList:
    print ("We need to find some users!")

for x in userList:
    if x == "admin":
        print ("Hello " + x + ", would you like to see a status report?")
    else:
        print ("Welcome " + x + ", thank you for logging in again.")