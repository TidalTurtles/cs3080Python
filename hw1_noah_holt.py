# Homework_1
# Noah_Holt
# Due: 2 sept 2022
# Security Program
#   Ask the user a series of questions and see if they can answer them

# Needed
#   1) min 1 print(Y), input(Y), str(Y), len(Y), int(N) randint(Y)
#   2) one var for int (Y), float (Y) and string (Y)
#   3) pick camelcase (Y) or underscores (N)
#   4) use 4 math operations (one must be % or //) (3)
#   5) use for loop to ask 3 question and use the range() (use i for the questions)  (Y)
#   6) need one each of if, elif, else, break, continue  (Y)
#   7) need one truthy or falsey (Y)
#   8) Comment it good

# Think the struggle will be to use the len() and randint() and continue
# truthy and falsey a bit confusing still so need to look that up also

# Ideas for creativity:  Make it about something I like. Like Disc Golf

import random

# will use later for calcs
theDistance = random.randint(50, 1000)

name = ''
# till it's my name
while not name:
    print("So, what is your name?")
    name = input()

print("Seems like you like disc golf")

nameSpeed = len(name)
print("if your name was a disc, it would be " + str(nameSpeed) + " speed")
print()

# putters are 0-4, mid are 5-8, drivers are else
if nameSpeed < 5:
    print("that makes you a putter!")
    howFar = 50
elif nameSpeed < 8:
    print("that makes you a midrange!")
    howFar = 150
else:
    print("that makes you a driver!")
    howFar = 250

# Let's see how much it would take to make the hole with a disc with the speed of the name length
throwYourselfRounded = theDistance // howFar
throwYourselfLeftOvers = theDistance % howFar
throwYourselfFloat = theDistance / 150 # this is a float

print("If you threw you as a disc on a " + str(theDistance) + "ft hole...")
print("It takes the average player " + str(throwYourselfFloat) + "throws to make it!")
print()
print("It would take " + str(throwYourselfRounded) + " throws!")
print("That leaves only " + str(throwYourselfLeftOvers) + "ft still to go!!")
print()

# lets build a bag to go play
favoriteDiscs = []
for i in range(4):
    print("What is your number " + str(i + 1) + " disc?")
    favoriteDiscs = favoriteDiscs + [input()]

print("In your disc golf bag is a:")
for disc in favoriteDiscs:
    print(" " + disc)
print("That's a great start!!!")
