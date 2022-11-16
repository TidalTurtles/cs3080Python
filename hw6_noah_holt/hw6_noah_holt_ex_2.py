'''
Noah Holt
cs 3020 Python
Homework 6
Exercise 2: Fibonacci (but better)
    using given fibonacci function
    make decorator to improve run time as it is slow.
    implement @cache decorator
    apply @countCalls
    write conclusion at top describing difference
'''


'''
Conclusion:
    
'''


def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(7))
