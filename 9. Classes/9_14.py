from random import randint
def get_winning_ticket_number(possible_list):
    stringPlace = ""
    numString = ""
    alphaString = ""

    for i in range(0,4):
        numString += possible_list[randint(0, 9)]
        alphaString += possible_list[randint(10, 13)]
    stringPlace = numString + alphaString
    return stringPlace



series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]
winning_ticket_list = []
for i in range(0,10):
    winning_ticket_list.append(get_winning_ticket_number(series))

print(winning_ticket_list)