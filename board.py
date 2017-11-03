import numpy as np

board = np.board = [
    [' ','1','2','3','4','5','6','7','8'],
    ['1','B','*','B','*','B','*','B','*'],
    ['2','*','B','*','B','*','B','*','B'],
    ['3','B','*','B','*','B','*','B','*'],
    ['4','*','*','*','*','*','*','*','*'],
    ['5','*','*','*','*','*','*','*','*'],
    ['6','W','*','W','*','W','*','W','*'],
    ['7','*','W','*','W','*','W','*','W'],
    ['8','W','*','W','*','W','*','W','*']
    ]

for rows in board:
    print rows
def blackmove(board):
    while True:
        counterPlaceBX = input("BLACK - Input the X coordinate for the counter you want to move")
        counterPlaceBY = input("BLACK - Input the Y coordinate for the counter you want to move")
        #counterPlaceSplit = counterPlace.split(',')
        if board[counterPlaceBX][counterPlaceBY] == "B":
            board[counterPlaceBX][counterPlaceBY] = '*'
        else:
            print("Not your counter")
            continue
        for rows in board:
            print rows
        while True:
            newCounterBX = input("BLACK - Input the X coordinate for the place you want to move")
            newCounterBY = input("BLACK - Input the Y coordinate for the place you want to move")

            if counterPlaceBY == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            elif board[newCounterBX][newCounterBY] is not board[counterPlaceBX+1][counterPlaceBY-1] or board[newCounterBX][newCounterBY] is not board[counterPlaceBX+1][counterPlaceBY+1]:
                print("Can't Move Here, You Can Only Move 1 Space")
                continue
            else:
                board[newCounterBX][newCounterBY] = 'B'
            break
        for rows in board:
            print rows

def whitemove(board):
    while True:
        counterPlaceWX = input("WHITE - Input the X coordinate for the counter you want to move")
        counterPlaceWY = input("WHITE - Input the Y coordinate for the counter you want to move")

        if board[counterPlaceWX][counterPlaceWY] == "W":
            board[counterPlaceWX][counterPlaceWY] = '*'
        else:
            print("Not your counter")
            continue
        for rows in board:
            print rows
        while True:
            newCounterWX = input("WHITE - Input the X coordinate for the place you want to move")
            newCounterWY = input("WHITE - Input the Y coordinate for the place you want to move")

            if counterPlaceWY == newCounterWY:
                print ("You Can Only Move Diagonally")
                continue
            elif board[newCounterWX][newCounterWY] is not board[counterPlaceWX-1][counterPlaceWY+1] or board[newCounterWX][newCounterWY] is not board[counterPlaceWX-1][counterPlaceWY-1]:
                print("Can't Move Here, You Can Only Move 1 Space")
                continue
            else:
                board[newCounterWX][newCounterWY] = 'W'
            break
        for rows in board:
            print rows
        break


#while counters on board !=1:
while True:
    whitemove(board)
    blackmove(board)
#if counter is blackmove
