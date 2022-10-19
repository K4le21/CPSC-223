all_users = ["Bob", "Tom", "Kevin"]
print (all_users)
all_users.append("Ralph")

untrusted_users = ["Bob", "Ben"]
print (untrusted_users)

trusted_users = []

for x in all_users:
    if x not in untrusted_users:
        trusted_users.append(x)

print (trusted_users)