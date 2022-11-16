'''
Noah Holt
cs 3020 Python
Homework 6
Exercise 1: Slow Down decorator
    write a @slowDown to sleep for number seconds passed
    default 1

    note:
        you can use @slowDown example from class and modify it
'''

import functools
import time


def slowDown(_func=None, *, second=1):
    def decorateSlowDown(func):
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(second)
            return func(*args, **kwargs)
        return wrapperSlowDown

    if _func is None:
        return decorateSlowDown
    else:
        return decorateSlowDown(_func)



@slowDown
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)


@slowDown(second=3)
def countdown2(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown2(fromNumber - 1)


countdown(5)
countdown2(3)
#slowDown(countdown(5), second=5)
