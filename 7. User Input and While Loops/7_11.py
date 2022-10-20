print(" x   x**2 x**3")

for x in range(1, 11):
    print(str(x) + " {squared} {cubed}".format(squared = x**2, cubed = x**3))