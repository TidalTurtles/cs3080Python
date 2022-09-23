# Homework_2_4
# Noah_Holt
# Due: 23 sept 2022
# guess number program
# 1) make random num between 1-20
# 2) big while loop till user input is random number
# 3) print that they are right at the number and guesses it took
#
# 2) More complicated
#    Make the upper and lower bound random as well
# 3) Now make computer guess
#    Make it a little smart

import random

# start vars
guessThis = random.randint(1, 21)
userGuess = 0
guessCount = 0
print("I'm thinking of a number...")

while userGuess != guessThis:
    print("Which number is it (hint: between 1-20)")
    guessCount += 1
    userGuess = int(input())
    if userGuess == guessThis:
        print("You guessed right!!! The number was " + str(userGuess))
    else:
        print("Nope, not quite. How about you try again!")


print("Nice job! it only took you " + str(guessCount) + " tries to guess!")
