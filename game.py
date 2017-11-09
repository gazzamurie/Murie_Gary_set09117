import numpy as np

board = np.board = [
    [' ','1','2','3','4','5','6','7','8'],
    ['1','B','*','B','*','B','*','B','*'],
    ['2','*','B','*','B','*','B','*','B'],
    ['3','B','*','B','*','B','*','B','*'],
    ['4','*','W','*','*','*','W','*','*'],
    ['5','*','*','*','*','*','*','*','*'],
    ['6','*','W','*','*','*','W','*','*'],
    ['7','W','*','W','*','B','*','W','*'],
    ['8','*','*','*','W','*','*','*','W']
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
        # try:
        counterPlaceBX = input("BLACK - Input the X coordinate for the counter you want to move: ")
        counterPlaceBY = input("BLACK - Input the Y coordinate for the counter you want to move: ")
        # except ValueError:
            # print("Cannot Take Value, Please Enter Number")
        #counterPlaceSplit = counterPlace.split(',')
        if board[counterPlaceBX][counterPlaceBY] == "B" or board[counterPlaceBX][counterPlaceBY] == "@":
            pass
        else:
            print("Not your counter")
            continue
        for rows in board:
            print rows

        while True:
            counterPlaceBXWhile = counterPlaceBX
            counterPlaceBYWhile = counterPlaceBY
            newCounterBX = input("BLACK - Input the X coordinate for the place you want to move: ")
            newCounterBY = input("BLACK - Input the Y coordinate for the place you want to move: ")
            #MAKES SURE THE BASIC COUNTER CAN ONLY MOVE FORWARD AND DIAGONALLY
            if board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile+1:
                print("Can't Move Here, You Can Only Move 1 Space(1)")
                continue
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile-1:
                print("Can't Move Here, You Can Only Move 1 Space(2)")
                continue
            elif counterPlaceBYWhile == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            #IF THE BASIC(BLACK) COUNTER REACHES THE END OF THE BOARD CHANGE THE COUNTER TO A KING REPRESENTED BY A @
            elif newCounterBX == 8:
                 print("8")
                 print newCounterBX
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = '@'
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY] == "W":
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY-1] = 'B'
                print("A")
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B'  and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY] == "W":
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                print("B")
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B':
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'B'
                 break

                #KINGS!!!!

            #ALLOWS THE KINGS TO MOVE IN ALL DIRECTIONS ONE SPACE
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@' and newCounterBX is not counterPlaceBXWhile-1 and newCounterBY is not counterPlaceBYWhile+1:
                print("Can't Move Here, You Can Only Move 1 Space(KK1)")
                pass
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@' and newCounterBX is not counterPlaceBXWhile-1 and newCounterBY is not counterPlaceBYWhile-1:
                print("Can't Move Here, You Can Only Move 1 Space(KK2)")
                pass
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@' and newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile+1:
                print("Can't Move Here, You Can Only Move 1 Space(K1)")
                pass
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@' and newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile-1:
                print("Can't Move Here, You Can Only Move 1 Space(K2)")
                pass
                break
            elif counterPlaceBYWhile == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            #ALLOWS THE KING TO JUMP OVER A WHITE COUNTER
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@' and counterPlaceBYWhile > newCounterBY and newCounterBX < counterPlaceBXWhile and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX-1][newCounterBY-1] = '@'
                 print("KC")
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@'  and counterPlaceBYWhile < newCounterBY and newCounterBX < counterPlaceBXWhile and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX-1][newCounterBY+1] = '@'
                 print("KD")
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX+1][newCounterBY-1] = '@'
                 print("KA")
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@'  and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX+1][newCounterBY+1] = '@'
                 print("KB")
                 break
             #ALLOWS THE KING TO MOVE WHILE KEEPING KING STATUS
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == '@':
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = '@'
                 break
            #IF NO CONDITIONS WERE MET IE NO JUMP OF NO KING TO CROWN THEN JUMP MOVE THE ONE SPACE
            else:
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX][newCounterBY] = 'B'
                break
                break
        for rows in board:
            print rows
        return board




# def whiteMove(board):
#     while True:
#         counterPlaceWX = input("WHITE - Input the X coordinate for the counter you want to move")
#         counterPlaceWY = input("WHITE - Input the Y coordinate for the counter you want to move")
#
#         if board[counterPlaceWX][counterPlaceWY] == "W":
#             pass
#         else:
#             print("Not your counter")
#             continue
#         for rows in board:
#             print rows
#         while True:
#             counterPlaceWXWhile = counterPlaceWX
#             counterPlaceWYWhile = counterPlaceWY
#             newCounterWX = input("WHITE - Input the X coordinate for the place you want to move")
#             newCounterWY = input("WHITE - Input the Y coordinate for the place you want to move")
#
#             if board[newCounterWX][newCounterWX] == "B" and newCounterWX > counterPlaceWXWhile:
#               board[newCounterWX][newCounterWY] = '*'
#               board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
#               board[newCounterWX-1][newCounterWY+1] = 'W'
#               break
#             elif board[newCounterWX][newCounterWX] == "B" and newCounterWX < counterPlaceWXWhile:
#                  board[newCounterWX][newCounterWY] = '*'
#                  board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
#                  board[newCounterWX-1][newCounterWY-1] = 'W'
#                  break
#             elif counterPlaceWYWhile == newCounterWY:
#                 print ("You Can Only Move Diagonally")
#                 continue
#             elif board[newCounterWX][newCounterWY] is not board[counterPlaceWXWhile-1][counterPlaceWYWhile+1] or board[newCounterWX][newCounterWY] is not board[counterPlaceWXWhile-1][counterPlaceWYWhile-1]:
#                 print("Can't Move Here, You Can Only Move 1 Space")
#                 print counterPlaceWXWhile
#                 print counterPlaceWYWhile
#                 continue
#             #elif white counter reeaches row 1 then become a king
#             #Might have to change/take this out of this if else to allow it to move backwards?
#             else:
#                 board[newCounterWX][newCounterWY] = 'W'
#                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
#                 break
#                 break
#         for rows in board:
#             print rows
#         return board

    #while counters on board !=1:
while True:
    blackMove(board)
    # whiteMove(board)
    # if board == "B":
    #     print("Black Wins")
    # else:
    #     print("White wins")
    # break
    #if counter is blackmove
