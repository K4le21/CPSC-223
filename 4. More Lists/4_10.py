largeList = list(range(1, 10+1))
cubedList = []

for x in largeList:
    cubedList.append(x**3)

print ("The first three items in the list are:")
print (cubedList[:3])
print ("Three items from the middle of the list are:")
print (cubedList[3:6])
print ("The last three items in the list are:")
print (cubedList[6:9])