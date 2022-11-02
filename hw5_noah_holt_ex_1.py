'''
Homework 5
Exercise 1
Noah Holt
Due: 9 nov 2022
Reverse Iterator
    make clas ReverseIter
        takes in list
        iterates backwards
'''

class ReverseIter:
    def __init__(self, ls):
        self.counter = len(ls) - 1
        self.ls = ls

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= 0:
            result = self.ls[self.counter]
            self.counter -= 1
            return result
        else:
            raise StopIteration()


it = ReverseIter([1, 2, 3, 4])
'''
Working
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
'''