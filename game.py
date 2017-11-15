import numpy as np
import sys

board = [
    [' ','1','2','3','4','5','6','7','8'],
    ['1','B','*','B','*','B','*','B','*'],
    ['2','*','B','*','B','*','B','*','B'],
    ['3','B','*','B','*','B','*','B','*'],
    ['4','*','*','*','*','*','W','*','*'],
    ['5','*','*','*','*','*','*','*','*'],
    ['6','*','*','*','*','*','*','*','*'],
    ['7','*','*','*','*','*','*','*','*'],
    ['8','*','*','*','*','*','*','*','*']
    ]
for rows in board:
    print rows

    white = 1
    whiteKing = white
    black = 12
    blackKing = black
# https://docs.python.org/2/tutorial/errors.html
#     while True:
#      try:
#          x = int(raw_input("Please enter a number: "))
#          break
#      except ValueError:
#          print "Oops!  That was no valid number.  Try again..."

def menu():
    print("MENU")

def blackMove(board):
    while True:
        # try:
        counterPlaceBX = input("BLACK - Input the X coordinate for the counter you want to move: ")
        counterPlaceBY = input("BLACK - Input the Y coordinate for the counter you want to move: ")
        # except ValueError:
            # print("Cannot Take Value, Please Enter Number")
        if board[counterPlaceBX][counterPlaceBY] == "B" or board[counterPlaceBX][counterPlaceBY] == "X":
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
            if newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile+1 and board[counterPlaceBXWhile][counterPlaceBYWhile]=='B':
                print("Can't Move Here, You Can Only Move 1 Space(1)")
                continue
            if newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile-1 and board[counterPlaceBXWhile][counterPlaceBYWhile]=='B':
                print("Can't Move Here, You Can Only Move 1 Space(2)")
                continue
            elif counterPlaceBYWhile == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            #IF THE BASIC(BLACK) COUNTER REACHES THE END OF THE BOARD CHANGE THE COUNTER TO A KING REPRESENTED BY A X
            elif newCounterBX == 8:
                 print("8")
                 print newCounterBX
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'X'
                 white-1
                 print whiteKing
                 break
             #Allows the basic black counter to jump over white counter
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY] == "W":
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY-1] = 'B'
                white-1
                print white
                print("A JUMP")
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B'  and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY] == "W":
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                white-1
                print white
                print("B JUMP")
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B':
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'B'
                 break
            #KINGS
            #ALLOWS THE KINGS TO MOVE IN ALL DIRECTIONS ONE SPACE
            if newCounterBX is not counterPlaceBXWhile-1 and newCounterBY is not counterPlaceBYWhile+1:
                print("Can't Move Here, You Can Only Move 1 Space(BACK RIGHT)")
                continue
                if newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile-1:
                    print("Can't Move Here, You Can Only Move 1 Space(FORAWRD LEFT)")
                    continue
                    if newCounterBX is not counterPlaceBXWhile-1 and newCounterBY is not counterPlaceBYWhile-1:
                        print("Can't Move Here, You Can Only Move 1 Space(BACK LEFT)")
                        continue
                        if newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile+1:
                            print("Can't Move Here, You Can Only Move 1 Space(FORWARD RIGHT)")
                            continue
            #ALLOWS THE KING TO JUMP OVER A WHITE COUNTER
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X' and counterPlaceBYWhile > newCounterBY and newCounterBX < counterPlaceBXWhile and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX-1][newCounterBY-1] = 'X'
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X'  and counterPlaceBYWhile < newCounterBY and newCounterBX < counterPlaceBXWhile and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX-1][newCounterBY+1] = 'X'
                 print("KD")
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX-1][newCounterBY-1] = 'X'
                 print("KA")
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X'  and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX+1][newCounterBY+1] = 'X'
                 print("KB")
                 break
             #ALLOWS THE KING TO MOVE WHILE KEEPING KING STATUS
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X':
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'X'
                 break
            #IF NO CONDITIONS WERE MET - IE NO JUMP OR NO KING TO CROWN THEN JUMP MOVE THE ONE SPACE
            else:
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX][newCounterBY] = 'B'
                print whiteKing
                print white
                print blackKing
                print black
                break
                break
        for rows in board:
            print rows
        return board

def whoWins(board):
    # print whiteKing
    # print white
    # print blackKing
    # print black
    # if white == 0:
    #     print("Black Wins")
    # if black == 0:
    #     print("White Wins")
    # else:
    #     print("ELSE")

     while True:
         if 'B' in board:
            print("B IN BOARD")
            break
         else:
            print("WHITE WINS")
            sys.exit()
         if 'W' in board:
            print("W IN BOARD")
            break
         else:
             print("WHITE WINS")
             sys.exit()

#def whiteMove(board):

while True:
    blackMove(board)
    whoWins(board)
    menu
    #whiteMove(board)
    # if board == "B":
    #     print("Black Wins")
    # else:
    #     print("White wins")
    # break
    #if counter is blackmove
