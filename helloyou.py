try:
    name = input ('What is your name? ')
    name = name.upper()
    print ("Hello, " + name + "!")
    print (("Your name has " + str(len(name)) + " letters in it! Awesome!").upper())
except ValueError:
    print('Please enter your name using letters only.')


# alternatively:
# user_name = input('What is your name? ')
# print("HELLO, " + user_name.upper() + "!")
# print("YOUR NAME HAS " + str(len(user_name)) + " LETTERS IN IT! AWESOME!")