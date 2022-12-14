def generic_sequence_func(p1, p2):
    """ What does this function do? """
    for i in range(p2):
        for e in p1[i]:
            print(e)

# Determine what parameters go into this function
try:
    generic_sequence_func(XXX,YYY)
       
#Multiple except blocks to handle Exceptions            
except NameError:
    print("Name Error")

except TypeError:
    print("Type Error")
    if not isinstance(XXX, list):
        print("Variable XXX is not a list.")
    if not isinstance(YYY, int):
        print("Variable YYY is not an int.")
