# Homework_1
# Noah_Holt
# Due: 2 sept 2022
# Security Program
#   Ask the user a series of questions and see if they can answer them

# Needed
#   1) min 1 print(Y), input(Y), str(N), len(N), int(N) randint(Y)
#   2) one var for int (Y), float (N) and string (Y)
#   3) pick camelcase (Y) or underscores (N)
#   4) use 4 math operations (one must be % or //)
#   5) use for loop to ask 3 question and use the range() (use i for the questions)
#   6) need one each of if, elif, else, break, continue
#   7) need one truthy or falsey
#   8) Comment it good

# Think the struggle will be to use the len() and randint() and continue
# truthy and falsey a bit confusing still so need to look that up also

# Ideas for creativity:  Guessing game with math or Lilo and Stitch alternate script (sounds fun but long)

import random

guessIt = random.randint(1, 21)

print("So, what is your name?")

nameGiven = input()  # this will be a string

print(nameGiven + " your number is " + str(guessIt))


