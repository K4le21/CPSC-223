largeList = list(range(2, 1000+1))

for x in largeList:
    for y in largeList:
        if (y%x == 0 and y != x):
            largeList.remove(y)

for x in largeList:
    print (x)