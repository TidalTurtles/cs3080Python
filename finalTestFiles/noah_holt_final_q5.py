'''

Generate a random integer between 1 and 10 (both inclusive)
and store it in a variable n. Do not hard code n.
Use a Generator function (NOT an object/class or a generator expression)
to generate the first n negative odd numbers starting from -1. For example,
your output for n = 5 would be:

The first 5 negative odd numbers are: -1 -3 -5 -7 -9

Print the values in the exact same style as above.
Please save your code firstname_lastname_final_q5.py

'''

import random

#borrowed from lectures
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def negatives():
    neg = -1
    for i in integers():
        if neg % 2 != 0:
            yield neg
        neg -= 1



n = random.randint(1, 11)

result = negatives()

for i in range(n):
    print(next(result))

