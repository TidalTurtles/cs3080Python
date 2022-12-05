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