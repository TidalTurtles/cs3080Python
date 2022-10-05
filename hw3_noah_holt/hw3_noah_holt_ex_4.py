# Homework_3_4
# Noah_Holt
# Due: 7 oct 2022
# Tic-Tac-Toe
#
# 1) create data structure (3x3 that has X,O, " " for values)
# 2) function to print board
# 3) make code for player input

# found help in book chapter 5
def printBoard(board):
    print(board['top-Left'] + ' | ' + board['top-Mid'] + ' | ' + board['top-Right'])
    print('- + - + -')
    print(board['mid-Left'] + ' | ' + board['mid-Mid'] + ' | ' + board['mid-Right'])
    print('- + - + -')
    print(board['low-Left'] + ' | ' + board['low-Mid'] + ' | ' + board['low-Right'])


def placeChar(board, character):
    place = input()
    board[place] = character



theBoard = {'top-Left': ' ', 'top-Mid': ' ', 'top-Right': ' ',
            'mid-Left': ' ', 'mid-Mid': ' ', 'mid-Right': ' ',
            'low-Left': ' ', 'low-Mid': ' ', 'low-Right': ' '}

printBoard(theBoard)

playing = True
putMeOnBoard = 'X'
# start with 6 moves so
count = 0

while playing:
    print("Time to place an " + putMeOnBoard + " on the board")
    placeChar(theBoard, putMeOnBoard)
    printBoard(theBoard)
    if putMeOnBoard == 'X':
        putMeOnBoard = 'O'
    else:
        putMeOnBoard = 'X'

    count = count + 1
    if count == 6:
        playing = False
