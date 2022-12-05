'''
Noah Holt
cs 3020 Python
Homework 7
due: 7 dec

Exercise 3: Simple Threads
    multi thread app

    In Main Thread:
        get int from user called numThreads
            ask until int >= 2
        make someFunc(i) to make different threads
        call someFunc(i) in for loop i = numThreads
            i is for loop AND i for someFunc

        For numThreads join() said threads

    other threads:
        using logging module print DEBUG level
        print "Welcome thread i"
        print "Number i is" "Even" or "Odd"
        sleep for 3 sec
        print "Goodbye thead i"

'''

import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(lineno)s - %(message)s')


def someFunc(i):
    logging.debug('Welcome thread {}'.format(i))
    if i % 2 == 0:
        logging.debug('Number {} is even'.format(i))
    else:
        logging.debug('Number {} is odd'.format(i))

    time.sleep(3)
    logging.debug('Goodbye thread {}'.format(i))


numThreads = None

while True:
    try:
        numThreads = int(input("How many threads will you create? (>= 2 please): "))
        if numThreads < 2:
            print("that number is to small")
        else:
            break
    except:
        print("That was not quite right.")

runningThread = [None] * numThreads
for thread in range(numThreads):
    runningThread[thread] = threading.Thread(target=someFunc, args=(thread, ))
    runningThread[thread].start()

for wire in range(numThreads):
    runningThread[wire].join()

