import sys

# board = [
#     [' ','1','2','3','4','5','6','7','8'],
#     ['1','B','*','B','*','B','*','B','*'],
#     ['2','*','B','*','B','*','B','*','B'],
#     ['3','B','*','B','*','B','*','B','*'],
#     ['4','*','*','*','*','*','*','*','*'],
#     ['5','*','*','*','*','*','*','*','*'],
#     ['6','*','W','*','W','*','W','*','W'],
#     ['7','W','*','W','*','W','*','W','*'],
#     ['8','*','W','*','W','*','W','*','W']
#     ]

board = [
[' ','1','2','3','4'],
['1','*','*','*','*'],
['2','*','B','*','*'],
['3','W','*','W','*'],
['4','*','*','*','*'],
]

# def menu():
#     print("                    MENU                 ")
#     print("             Player vs Player: Press 1   ")
#     print("                   Exit: Press 0         ")
#
# try:
#     num = int(input("enter number: "))
# except ValueError:
#     print("you must enter an integer")

def blackMove(board):
    while True:

        for rows in board:
            print rows
        try:
            counterPlaceBX = int(raw_input("BLACK - Input the X coordinate for the counter you want to move: "))
        except ValueError:
            print("You must enter an number.")
            continue
        try:
            counterPlaceBY = int(raw_input("BLACK - Input the Y coordinate for the counter you want to move: "))
        except ValueError:
            print("You must enter an number.")
            continue

        if board[counterPlaceBX][counterPlaceBY] == "B" or board[counterPlaceBX][counterPlaceBY] == "X":
            pass
        else:
            print("Not your counter.")
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
            if board[newCounterBX][newCounterBY] == 'B':
                print("Can't Move Here!")
                continue
            elif counterPlaceBYWhile == newCounterBY:
                print ("You Can Only Move Diagonally")
                continue
            elif counterPlaceBXWhile == newCounterBX:
                print ("You Can Only Move Diagonally")
                continue
             #Allows the basic black counter to jump over white counter
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY]=='W':
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY-1] = 'B'
                print("A JUMP")
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY]=='O':
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY-1] = 'B'
                print("A JUMP KING")
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY]=='W':
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                print("B JUMP")
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY]=='O' :
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                print("B JUMP KING")
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B':
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'B'
                 break
             #IF THE BASIC(BLACK) COUNTER REACHES THE END OF THE BOARD CHANGE THE COUNTER TO A KING REPRESENTED BY A X
            elif newCounterBX == 8:
                 print("8")
                 print newCounterBX
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'X'
                 break
            #KINGS
            #ALLOWS THE KINGS TO MOVE IN ALL DIRECTIONS ONE SPACE
            if newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile-1:
                print("Can't Move Here, You Can Only Move 1 Space(FORAWRD LEFT)")
                continue
                if newCounterBX is not counterPlaceBXWhile-1 and newCounterBY is not counterPlaceBYWhile+1:
                    print("Can't Move Here, You Can Only Move 1 Space(BACK RIGHT)")
                    continue
                    if newCounterBX is not counterPlaceBXWhile-1 and newCounterBY is not counterPlaceBYWhile-1:
                        print("Can't Move Here, You Can Only Move 1 Space(BACK LEFT)")
                        continue
                        if newCounterBX is not counterPlaceBXWhile+1 and newCounterBY is not counterPlaceBYWhile+1:
                            print("Can't Move Here, You Can Only Move 1 Space(FORWARD RIGHT)")
                            continue
                    else:
                        pass
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
                break
                break
            whoWins(board)
        # for rows in board:
        #     print rows
        # return board


def whiteMove(board):

    for rows in board:
        print rows

    while True:
        # try:
        counterPlaceWX = input("WHITE - Input the X coordinate for the counter you want to move: ")
        counterPlaceWY = input("WHITE - Input the Y coordinate for the counter you want to move: ")
        # except ValueError:
            # print("Cannot Take Value, Please Enter Number")
        if board[counterPlaceWX][counterPlaceWY] == "W" or board[counterPlaceWX][counterPlaceWY] == "O":
            pass
        else:
            print("Not your counter")
            continue
        for rows in board:
            print rows

        while True:
            counterPlaceWXWhile = counterPlaceWX
            counterPlaceWYWhile = counterPlaceWY
            newCounterWX = input("WHITE - Input the X coordinate for the place you want to move: ")
            newCounterWY = input("WHITE - Input the Y coordinate for the place you want to move: ")
            #MAKES SURE THE BASIC COUNTER CAN ONLY MOVE FORWARD AND DIAGONALLY
            if newCounterWX is not counterPlaceWXWhile-1 and newCounterWY is not counterPlaceWYWhile+1 and board[counterPlaceWXWhile][counterPlaceWYWhile]=='W':
                print("Can't Move Here, You Can Only Move 1 Space(1)")
                continue
            if newCounterWX is not counterPlaceWXWhile-1 and newCounterWY is not counterPlaceWYWhile-1 and board[counterPlaceWXWhile][counterPlaceWYWhile]=='W':
                print("Can't Move Here, You Can Only Move 1 Space(2)")
                continue
            if board[newCounterWX][newCounterWY] == 'W':
                print("Can't Move Here!")
                continue
            elif counterPlaceWYWhile == newCounterWY:
                print ("You Can Only Move Diagonally")
                continue
            elif counterPlaceWXWhile == newCounterWX:
                print ("You Can Only Move Diagonally")
                continue
            #IF THE BASIC(WHITE) COUNTER REACHES THE END OF THE BOARD CHANGE THE COUNTER TO A KING REPRESENTED BY A O
            elif newCounterWX == 1:
                 print("Row 1")
                 print newCounterWX
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX][newCounterWY] = 'O'
                 break
             #Allows the basic black counter to jump over white counter
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile > newCounterWY and board[newCounterWX][newCounterWY] == "B":
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY-1] = 'W'
                print("A JUMP WHITE")
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile > newCounterWY and board[newCounterWX][newCounterWY] == "X":
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY-1] = 'W'
                print("A JUMP KING")
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile < newCounterWY and board[newCounterWX][newCounterWY] == 'B':
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY+1] = 'W'
                print("B JUMP WHITE")
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile < newCounterWY and board[newCounterWX][newCounterWY] == 'X':
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY+1] = 'W'
                print("B JUMP KING")
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W':
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX][newCounterWY] = 'W'
                 break
            #KINGS
            #ALLOWS THE KINGS TO MOVE IN ALL DIRECTIONS ONE SPACE
            if newCounterWX is not counterPlaceWXWhile-1 and newCounterWY is not counterPlaceWYWhile+1:
                print("Can't Move Here, You Can Only Move 1 Space(BACK RIGHT)")
                continue
                if newCounterWX is not counterPlaceWXWhile+1 and newCounterWY is not counterPlaceWYWhile-1:
                    print("Can't Move Here, You Can Only Move 1 Space(FORAWRD LEFT)")
                    continue
                    if newCounterWX is not counterPlaceWXWhile-1 and newCounterWY is not counterPlaceWYWhile-1:
                        print("Can't Move Here, You Can Only Move 1 Space(BACK LEFT)")
                        continue
                        if newCounterWX is not counterPlaceWXWhile+1 and newCounterWY is not counterPlaceWYWhile+1:
                            print("Can't Move Here, You Can Only Move 1 Space(FORWARD RIGHT)")
                            continue
            #ALLOWS THE KING TO JUMP OVER A WHITE COUNTER
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O' and counterPlaceWYWhile > newCounterWY and newCounterWX < counterPlaceWXWhile and board[newCounterWX][newCounterWY] == "B":
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX-1][newCounterWY-1] = 'O'
                 break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O'  and counterPlaceWYWhile < newCounterWY and newCounterWX < counterPlaceWXWhile and board[newCounterWX][newCounterWY] == "B":
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX-1][newCounterWY+1] = 'O'
                 print("KD")
                 break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O' and counterPlaceWYWhile > newCounterWY and board[newCounterWX][newCounterWY] == "B":
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX-1][newCounterWY-1] = 'O'
                 print("KA")
                 break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O'  and counterPlaceWYWhile < newCounterWY and board[newCounterWX][newCounterWY] == "B":
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX+1][newCounterWY+1] = 'O'
                 print("KB")
                 break
             #ALLOWS THE KING TO MOVE WHILE KEEPING KING STATUS
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O':
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX][newCounterWY] = 'O'
                 break
            #IF NO CONDITIONS WERE MET - IE NO JUMP OR NO KING TO CROWN THEN JUMP MOVE THE ONE SPACE
            else:
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX][newCounterWY] = 'W'
                break
                break
            whoWins(board)
        for rows in board:
            print rows
        return board



def whoWins(board):
    while True:
        whiteWin=0
        blackWin=0
        #Check all the items in the array and see if it can find an W or O
        for i in range (5):
            for j in range(5):
                if board[i][j] == 'W':
                    #If it does add 1 to a vairiable(declared and set to 0 up top)
                    whiteWin = whiteWin + 1
        for i in range (5):
            for j in range(5):
                if board[i][j] == 'O':
                    whiteWin = whiteWin + 1
        #If 1 is not added to the vairiable then its equal to zero, which means there is no W or O counter on the board so Black counter wins
        if whiteWin == 0:
            print("       '||''|.   '||                  '||         '|| '||'  '|'  ||                   ")
            print("        ||   ||   ||   ....     ....   ||  ..      '|. '|.  .'  ...  .. ...    ....   ")
            print("        ||'''|.   ||  '' .||  .|   ''  || .'        ||  ||  |    ||   ||  ||  ||. '   ")
            print("        ||    ||  ||  .|' ||  ||       ||'|.         ||| |||     ||   ||  ||  . '|..  ")
            print("       .||...|'  .||. '|..'|'  '|...' .||. ||.        |   |     .||. .||. ||. |'..|'  ")
            break

        for i in range (5):
            for j in range(5):
                if board[i][j] == 'B':
                    blackWin = blackWin + 1
        for i in range (5):
            for j in range(5):
                if board[i][j] == 'X':
                    blackWin = blackWin + 1
        if blackWin == 0:
            print("      '|| '||'  '|' '||       ||    .              '|| '||'  '|'  ||                  ")
            print("       '|. '|.  .'   || ..   ...  .||.    ....      '|. '|.  .'  ...  .. ...    ....  ")
            print("        ||  ||  |    ||' ||   ||   ||   .|...||      ||  ||  |    ||   ||  ||  ||. '  ")
            print("         ||| |||     ||  ||   ||   ||   ||            ||| |||     ||   ||  ||  . '|.. ")
            print("          |   |     .||. ||. .||.  '|.'  '|...'        |   |     .||. .||. ||. |'..|' ")

            break
        break

while True:
    # blackMove(board)
    # whoWins(board)
    whiteMove(board)
    whoWins(board)
