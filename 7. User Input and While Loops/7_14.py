famousInfo = {"Lennon" : {
                "First Name" : "John",
                "Date of Birth" : "October 9, 1940",
                "Birthplace" : "Liverpool, United Kingdom",
                "Quote" : "Life is what happens when you're busy making other plans."},
        "Disney" : {
            "First Name" : "Walt",
            "Date of Birth" : "December 5, 1901",
            "Birthplace" : "Hermosa, U.S.A.",
            "Quote" : "The way to get started is to quit talking and begin doing."},
        "Mandela" : {
            "First Name" : "Nelson",
            "Date of Birth" : "July 18, 1918",
            "Birthplace" : "Mvezo, South Africa",
            "Quote" : "The greatest glory in living lies not in never falling, but in rising every time we fall."}}

print ("{0:<20} {1:<20} {2:<30} {3:<35}".format("Name", "Birthdate", "Birthplace", "Quote"))

for key, dictionary in famousInfo.items():
    print ("{0:<20} {1:<20} {2:<30} {3:<35}".format(key + ", " + dictionary["First Name"],  dictionary["Date of Birth"], dictionary["Birthplace"], dictionary["Quote"]))