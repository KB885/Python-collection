import numpy as np

# The board is 9x9
board = [
    [8,0,0,0,0,0,0,0,0], # 1
    [0,0,3,6,0,0,0,0,0], # 2
    [0,7,0,0,9,0,2,0,0], # 3
    [0,5,0,0,0,7,0,0,0], # 4
    [0,0,0,0,4,5,7,0,0], # 5
    [0,0,0,1,0,0,0,3,0], # 6
    [0,0,1,0,0,0,0,6,8], # 7
    [0,0,8,5,0,0,0,1,0], # 8
    [0,9,0,0,0,0,4,0,0] # 9
]

def possible(row, column, number):
    global board

    for i in range(0,9):
        if board[row][i] == number:
            return False

    for i in range(0,9):
        if board[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == number:
                return False
    return True

def solve():
    global board
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0
                return

    print(np.matrix(board))

solve()
