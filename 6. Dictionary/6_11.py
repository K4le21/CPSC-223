cities = {"Los Angeles" : {
                "Country" : "United States",
                "Population" : "3.973 million",
                "Fact" : "Los Angeles is the only North American city to have hosted the Olympics twice."},
        "Hong Kong" : {
            "Country" : "China",
            "Population" : "7.482 million",
            "Fact" : "Chinese (Cantonese) and English are the official languages of Hong Kong."},
        "Tokyo" : {
            "Country" : "Japan",
            "Population" : "13.96 million",
            "Fact" : "Tokyo Has Been the Japanese Capital Since 1868."}}

for key, dictionary in cities.items():
    print (key + " is located in " + dictionary["Country"] + ".")
    print ("The population of " + key + " is " + dictionary["Population"] + ".")
    print ("One fun fact about " + key + " is: " + dictionary["Fact"])