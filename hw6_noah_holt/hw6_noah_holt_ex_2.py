"""
Noah Holt
cs 3020 Python
Homework 6
Exercise 2: Fibonacci (but better)
    using given fibonacci function
    make decorator to improve run time as it is slow.
    implement @cache decorator
    apply @countCalls
    write conclusion at top describing difference
"""


"""
Conclusion:
    

"""

import functools


# stolen from lecture 9 notes
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls


def cache(func):
    def wrapperCache(*args, **kwargs):
        oldRuns = []
        
        return func(*args, **kwargs)
    return wrapperCache


@countCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(10))
print(fibonacci.numCalls)
