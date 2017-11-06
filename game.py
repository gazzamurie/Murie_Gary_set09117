import numpy as np

board = np.board = [
    [' ','1','2','3','4','5','6','7','8'],
    ['1','B','*','B','*','B','*','B','*'],
    ['2','*','B','*','B','*','B','*','B'],
    ['3','B','*','B','*','B','*','B','*'],
    ['4','*','*','*','*','*','*','*','*'],
    ['5','*','*','*','*','*','*','*','*'],
    ['6','*','W','*','W','*','W','*','W'],
    ['7','W','*','W','*','W','*','W','*'],
    ['8','*','W','*','W','*','W','*','W']
    ]
for rows in board:
    print rows

def blackMove(board):
    while True:
        counterPlaceBX = input("BLACK - Input the X coordinate for the counter you want to move")
        counterPlaceBY = input("BLACK - Input the Y coordinate for the counter you want to move")
        #counterPlaceSplit = counterPlace.split(',')
        if board[counterPlaceBX][counterPlaceBY] == "B":
            pass
        else:
            print("Not your counter")
            continue
        for rows in board:
            print rows

        while True:
            counterPlaceBXWhile = counterPlaceBX
            counterPlaceBYWhile = counterPlaceBY
            newCounterBX = input("BLACK - Input the X coordinate for the place you want to move")
            newCounterBY = input("BLACK - Input the Y coordinate for the place you want to move")

            if board[newCounterBX][newCounterBX] == "W" and newCounterBX > counterPlaceBXWhile:
                  board[newCounterBX][newCounterBY] = '*'
                  board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                  board[newCounterBX+1][newCounterBY+1] = 'B'
                  print board[newCounterBX][newCounterBY]
                  print board[counterPlaceBXWhile][counterPlaceBYWhile]
                  print board[newCounterBX+2][newCounterBY+2]
                  print("magic")
                  break
            elif counterPlaceBYWhile == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            elif board[newCounterBX][newCounterBY] is not board[counterPlaceBXWhile+1][counterPlaceBYWhile+1] or board[newCounterBX][newCounterBY] is not board[counterPlaceBXWhile+1][counterPlaceBYWhile-1]:
                print("Can't Move Here, You Can Only Move 1 Space")
                continue
            else:
             board[newCounterBX][newCounterBY] = 'B'
             board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
            break
            break
        for rows in board:
            print rows
        return board


def whiteMove(board):
    while True:
        counterPlaceWX = input("WHITE - Input the X coordinate for the counter you want to move")
        counterPlaceWY = input("WHITE - Input the Y coordinate for the counter you want to move")

        if board[counterPlaceWX][counterPlaceWY] == "W":
            pass
        else:
            print("Not your counter")
            continue
        for rows in board:
            print rows
        while True:
            counterPlaceWXWhile = counterPlaceWX
            counterPlaceWYWhile = counterPlaceWY
            newCounterWX = input("WHITE - Input the X coordinate for the place you want to move")
            newCounterWY = input("WHITE - Input the Y coordinate for the place you want to move")

            if counterPlaceWYWhile == newCounterWY:
                print ("You Can Only Move Diagonally")
                continue
            elif board[newCounterWX][newCounterWX] == "B":
                print("Counter To Jump")
                continue
            elif board[newCounterWX][newCounterWY] is not board[counterPlaceWXWhile-1][counterPlaceWYWhile+1] or board[newCounterWX][newCounterWY] is not board[counterPlaceWXWhile-1][counterPlaceWYWhile-1]:
                print("Can't Move Here, You Can Only Move 1 Space")
                continue
            else:
                board[newCounterWX][newCounterWY] = 'W'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                break
                break
        for rows in board:
            print rows
        return board

    #while counters on board !=1:
while True:
    blackMove(board)
    whiteMove(board)
    #if counter is blackmove
