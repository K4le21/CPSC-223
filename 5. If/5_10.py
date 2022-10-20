current_users = ["Will", "John", "David", "Mary", "Josh"]
new_users = ["mark", "harry", "will", "josh", "alex"]
lower_new_users = []

for x in new_users:
    x.lower()

for x in current_users:
    if x.lower() in new_users:
        print (x + " is taken. Please try another username")
    else:
        print (x + " is a valid username.")