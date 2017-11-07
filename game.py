import numpy as np

board = np.board = [
    [' ','1','2','3','4','5','6','7','8'],
    ['1','B','*','B','*','B','*','B','*'],
    ['2','*','B','*','B','*','B','*','B'],
    ['3','B','*','B','*','B','*','B','*'],
    ['4','*','*','*','*','*','*','*','*'],
    ['5','*','*','*','*','*','*','*','*'],
    ['6','*','W','*','W','*','W','*','W'],
    ['7','W','*','W','*','B','*','W','*'],
    ['8','*','W','*','W','*','*','*','W']
    ]
for rows in board:
    print rows


# https://docs.python.org/2/tutorial/errors.html
#     while True:
#      try:
#          x = int(raw_input("Please enter a number: "))
#          break
#      except ValueError:
#          print "Oops!  That was no valid number.  Try again..."

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

            if newCounterBX == 8:
                print("Youve Been Kinged")
            elif board[newCounterBX][newCounterBX] == "W" and newCounterBX > counterPlaceBXWhile:
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                break
            elif board[newCounterBX][newCounterBX] == "W" and newCounterBX < counterPlaceBXWhile:
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX+1][newCounterBY-1] = 'B'
                 break
            elif counterPlaceBYWhile == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            elif board[newCounterBX][newCounterBY] is not board[counterPlaceBXWhile+1][counterPlaceBYWhile+1] or board[newCounterBX][newCounterBY] is not board[counterPlaceBXWhile+1][counterPlaceBYWhile-1]:
                print("Can't Move Here, You Can Only Move 1 Space")
                print counterPlaceBXWhile
                print counterPlaceBYWhile
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

            if board[newCounterWX][newCounterWX] == "B" and newCounterWX > counterPlaceWXWhile:
              board[newCounterWX][newCounterWY] = '*'
              board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
              board[newCounterWX-1][newCounterWY+1] = 'W'
              break
            elif board[newCounterWX][newCounterWX] == "B" and newCounterWX < counterPlaceWXWhile:
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX-1][newCounterWY-1] = 'W'
                 break
            elif counterPlaceWYWhile == newCounterWY:
                print ("You Can Only Move Diagonally")
                continue
            elif board[newCounterWX][newCounterWY] is not board[counterPlaceWXWhile-1][counterPlaceWYWhile+1] or board[newCounterWX][newCounterWY] is not board[counterPlaceWXWhile-1][counterPlaceWYWhile-1]:
                print("Can't Move Here, You Can Only Move 1 Space")
                print counterPlaceWXWhile
                print counterPlaceWYWhile
                continue
            #elif white counter reeaches row 1 then become a king
            #Might have to change/take this out of this if else to allow it to move backwards?
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
    # if board == "B":
    #     print("Black Wins")
    # else:
    #     print("White wins")
    # break
    #if counter is blackmove
