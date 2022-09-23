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

# start var
lowerLimit = random.randint(1, 51)
upperLimit = random.randint(51, 101)
guessThis = random.randint(lowerLimit, upperLimit)
userGuess = 0
guessCount = 0
computerGuesses = [0]

print("I'm thinking of a number...")

while userGuess != guessThis and guessCount < 10:
    print(computerGuesses)
    print("Which number is it (hint: between (" + str(lowerLimit) + "-" + str(upperLimit) + ") You have 10 guesses!")
    guessCount += 1

    guessedThat = True
    while guessedThat:
        userGuess = random.randint(lowerLimit, upperLimit)
        found = 0
        for guess in computerGuesses:
            if guess == userGuess:
                found = 1
        if found == 0:
            guessedThat = False

    computerGuesses.append(userGuess)
    print("I will guess " + str(userGuess))

    if userGuess == guessThis:
        print("You guessed right!!! The number was " + str(userGuess))
    else:
        print("Nope, not quite. How about you try again!")

if guessCount < 10:
    print("Nice job! it only took you " + str(guessCount) + " tries to guess!")
else:
    print("Sorry,  the number I was thinking of was " + str(guessThis))