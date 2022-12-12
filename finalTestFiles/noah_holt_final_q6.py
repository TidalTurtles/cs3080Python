'''

Define a string variable with value 'Hello World!'.
Create an @uppercase decorator that will
convert this string to all uppercase 'HELLO WORLD!'.
Note: you cannot hard code 'HELLO WORLD!' in the decorator.

Use a regular function printStr() that prints your string variable,
and it will be decorated with your @uppercase decorator.
Call the decorated printStr() to test your result.

Please save your code as firstname_lastname_final_q6.py

'''


def uppercase(func):
    def wrapper(*args, **kwargs):
        printMe = str(args)
        func(printMe.upper())
    return wrapper


@uppercase
def printStr(message):
    print(message)


phrase = 'Hello World!'
printStr(phrase)
