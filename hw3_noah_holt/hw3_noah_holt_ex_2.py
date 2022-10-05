# Homework_3_2
# Noah_Holt
# Due: 7 oct 2022
# Number of Occurrences
#
# 1) count number of occurrences for each letter in a string
# 2) store in dictionary
# 3) print with pprint (see example on assignment)

import pprint

# test case: The quick brown fox jumps over the lazy dog.
# contains all letters

testString = "My name is Noah Holt. I am vegan!"

# initialize dictionary
lettersCounted = {}

# found similar in book chapter 5
# in the setDefault section
for character in testString:
    lettersCounted.setdefault(character, 0)
    lettersCounted[character] = lettersCounted[character] + 1

pprint.pprint(lettersCounted)
