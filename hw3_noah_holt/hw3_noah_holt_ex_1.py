# Homework_3_1
# Noah_Holt
# Due: 7 oct 2022
# Picture Grid
#
# 1) make grid
# 2) set to picture (see assignment)
# 3) print

lovelyPicture = [['.', '.', '.', '.', '.', '.'],
                 ['.', 'O', 'O', '.', '.', '.'],
                 ['O', 'O', 'O', 'O', '.', '.'],
                 ['O', 'O', 'O', 'O', 'O', '.'],
                 ['.', 'O', 'O', 'O', 'O', 'O'],
                 ['O', 'O', 'O', 'O', 'O', '.'],
                 ['O', 'O', 'O', 'O', '.', '.'],
                 ['.', 'O', 'O', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.']]

# maybe write columns and row lengths as not working as for item in list
columns = len(lovelyPicture)
rows = len(lovelyPicture[0])

'''
Hint:  You  will  need  to  use  a  loop  in  a  loop  in  order  to  print  grid[0][0],
then  grid[1][0],  then grid[2][0], and so on, up to grid[8][0]. 
This will finish the first row, so then print a newline.
Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
The last thing your program will print is grid[8][5]. 
Also, remember to pass the end keyword argument to print() 
if  you  don’t  want  a  newline  printed  automatically  after  each  print()  call. 
'''

# issue I experience: It stops at column 6, not sure why (error: out of range)
# resolution: I had swapped the rows and columns in range and
# that was what was causing the out of range error
for y in range(rows):

    for x in range(columns):

        print(lovelyPicture[x][y], end=' ')

    print("")
