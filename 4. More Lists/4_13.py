buffet_menu = ("pizza", "rice", "mac and cheese", "spagetti", "french fries")

for x in buffet_menu:
    print (x)

#buffet_menu[1] = "chicken wings"
#This causes a traceback error when running.

buffet_menu = ("pizza", "chicken wings", "mac and cheese", "spagetti", "tater tots")
for x in buffet_menu:
    print (x)