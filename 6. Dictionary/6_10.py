fav_num = {"Jake" : [33, 23],
            "Bob" : [45, 99, 21] ,
            "Dylan" : [52],
            "Kevin" : [87, 67],
            "Mike": [13]}

for key, value in fav_num.items():
    if len(value) > 1:
        print(key + "'s favorite numbers are: " + str(value))
    else:
        print(key + "'s favorite number is " + str(value) + ".")