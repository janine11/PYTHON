#same as last one but there is a shorter one

# accept an input from 0-6 to correspond to each day of the week
day = int(input("Day(0-6"))

# if range
if day in range(1,6):
    print("Go to work!")

# elif day
elif day == 0 or day == 6:
    print("sleep in!") 

# else print
else:
    print("try again!")
