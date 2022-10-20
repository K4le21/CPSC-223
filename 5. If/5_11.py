largeList = list(range(1, 9+1))
for x in largeList:
    if x == 1:
        print (str(x) + "st")
    elif x == 2:
        print (str(x) + "nd")
    elif x == 3:
        print (str(x) + "rd")
    else:
        print (str(x) + "th")