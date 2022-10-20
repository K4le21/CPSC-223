favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

poll_list = ["gary", "edward", "mike", "phil", "jen"]

for x in poll_list:
    if x in favorite_languages.keys():
        print (x.title() + ", thank you for taking our poll.")
    else:
        print (x.title() + ", please take out poll.")
