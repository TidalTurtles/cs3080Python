'''
Noah Holt
cs 3020 Python
Homework 7
due: 7 dec

Exercise 1: Rename Files with Dates
    Needed:
        Search for all file names (*MM-DD-YYYY*)
        on find:
            change name to *YYYY-MM-DD*

    Do following:
        create regex
            Note: MM is 01-12 and DD is 01-31
            can make test files to judge
        call os.listdir() to find files in CURRENT directory
        loop over all and find American
        to rename call shutil.move()
'''

import re
import os
import shutil

americanDateRegex = re.compile(r'(.*)([01][0-9])-([0123][0-9])-([012][0-9][0-9][0-9])(.*)')

fileList = os.listdir('.')

for file in fileList:
    datePresent = americanDateRegex.search(file)
    if datePresent is not None:
        asianDate = '{}{}-{}-{}{}'.format(datePresent.group(1), datePresent.group(4), datePresent.group(2), datePresent.group(3), datePresent.group(5))
        shutil.copy(file, asianDate)


