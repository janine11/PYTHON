name = input('Name: ')
subject = input('Subject: ')

# fstrings
# story = f"{name}'s fav subject is {subject}"

story = "%s's fav subject is %s. %d" % (name, subject, 10) 

print(story)