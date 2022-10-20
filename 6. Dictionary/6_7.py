friend_info_1 = {"First name" : "James",
                "Last name" : "Lee",
                "Age" : 20,
                "City" : "Fullerton"}

friend_info_2 = {"First name" : "Josh",
                "Last name" : "Kim",
                "Age" : 19,
                "City" : "Anaheim"}

friend_info_3 = {"First name" : "Jason",
                "Last name" : "Park",
                "Age" : 21,
                "City" : "Fullerton"}



friends_info = [friend_info_1, friend_info_2, friend_info_3]

for i in friends_info:
    print (i.get("First name") + " " + i.get("Last name") + " is " + str(i.get("Age")) + " years old and lives in the city of " + i.get("City") + ".")
