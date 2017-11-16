import sys

board = [
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
            try:
                newCounterBX = int(raw_input("BLACK - Input the X coordinate for the place you want to move: "))
            except ValueError:
                print("You must enter an number.")
                continue
            try:
                newCounterBY = int(raw_input("BLACK - Input the Y coordinate for the place you want to move: "))
            except ValueError:
                print("You must enter an number.")
                continue
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
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY]=='O':
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY-1] = 'B'
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY]=='W':
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B' and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY]=='O' :
                board[newCounterBX][newCounterBY] = '*'
                board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                board[newCounterBX+1][newCounterBY+1] = 'B'
                whoWins(board)
                break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'B':
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX][newCounterBY] = 'B'
                 whoWins(board)
                 break
             #IF THE BASIC(BLACK) COUNTER REACHES THE END OF THE BOARD CHANGE THE COUNTER TO A KING REPRESENTED BY A X
            elif newCounterBX == 8:
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
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X' and counterPlaceBYWhile > newCounterBY and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX-1][newCounterBY-1] = 'X'
                 break
            elif board[counterPlaceBXWhile][counterPlaceBYWhile] == 'X'  and counterPlaceBYWhile < newCounterBY and board[newCounterBX][newCounterBY] == "W":
                 board[newCounterBX][newCounterBY] = '*'
                 board[counterPlaceBXWhile][counterPlaceBYWhile] = '*'
                 board[newCounterBX+1][newCounterBY+1] = 'X'
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
        break


def whiteMove(board):
    for rows in board:
        print rows

    while True:

        try:
            counterPlaceWX = int(raw_input("WHITE - Input the X coordinate for the counter you want to move: "))
        except ValueError:
            print("You must enter an number.")
            continue
        try:
            counterPlaceWY = int(raw_input("WHITE - Input the Y coordinate for the counter you want to move: "))
        except ValueError:
            print("You must enter an number.")
            continue

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
            try:
                newCounterWX = int(raw_input("WHITE - Input the X coordinate for the place you want to move: "))
            except ValueError:
                print("You must enter an number.")
                continue
            try:
                newCounterWY = int(raw_input("WHITE - Input the Y coordinate for the place you want to move: "))
            except ValueError:
                print("You must enter an number.")
                continue
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
                 print newCounterWX
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX][newCounterWY] = 'O'
                 break
             #Allows the basic black counter to jump over white counter
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile > newCounterWY and board[newCounterWX][newCounterWY] == "B":
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY-1] = 'W'
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile > newCounterWY and board[newCounterWX][newCounterWY] == "X":
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY-1] = 'W'
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile < newCounterWY and board[newCounterWX][newCounterWY] == 'B':
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY+1] = 'W'
                whoWins(board)
                break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'W' and counterPlaceWYWhile < newCounterWY and board[newCounterWX][newCounterWY] == 'X':
                board[newCounterWX][newCounterWY] = '*'
                board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                board[newCounterWX-1][newCounterWY+1] = 'W'
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
                 break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O' and counterPlaceWYWhile > newCounterWY and board[newCounterWX][newCounterWY] == "B":
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX-1][newCounterWY-1] = 'O'
                 break
            elif board[counterPlaceWXWhile][counterPlaceWYWhile] == 'O'  and counterPlaceWYWhile < newCounterWY and board[newCounterWX][newCounterWY] == "B":
                 board[newCounterWX][newCounterWY] = '*'
                 board[counterPlaceWXWhile][counterPlaceWYWhile] = '*'
                 board[newCounterWX+1][newCounterWY+1] = 'O'
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
        break

def whoWins(board):
    while True:
        whiteWin=0
        blackWin=0
        #Check all the items in the array and see if it can find an W or O
        for i in range (9):
            for j in range(9):
                if board[i][j] == 'W':
                    #If it does add 1 to a vairiable(declared and set to 0 up top)
                    whiteWin = whiteWin + 1
        for i in range (9):
            for j in range(9):
                if board[i][j] == 'O':
                    whiteWin = whiteWin + 1
        #If 1 is not added to the vairiable then its equal to zero, which means there is no W or O counter on the board so Black counter wins
        if whiteWin == 0:
            print("       '||''|.   '||                  '||         '|| '||'  '|'  ||                   ")
            print("        ||   ||   ||   ....     ....   ||  ..      '|. '|.  .'  ...  .. ...    ....   ")
            print("        ||'''|.   ||  '' .||  .|   ''  || .'        ||  ||  |    ||   ||  ||  ||. '   ")
            print("        ||    ||  ||  .|' ||  ||       ||'|.         ||| |||     ||   ||  ||  . '|..  ")
            print("       .||...|'  .||. '|..'|'  '|...' .||. ||.        |   |     .||. .||. ||. |'..|'  ")
            menu()
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
            menu()
            break
        break

def htPlay():
    print("         Player 1s counters are represented by B for regular counters and X for King counters.       ")
    print("         Player 2s counters are represented by W for regular counters and O for King counters.       ")
    print("      The game will ask the user to input the X and Y coordinates of the counter you want to move.   ")
    print("                     The X coordinate is the row and the Y coordinate is the column.                 ")
    print("                       The aim of the game is to get rid of all opponents counters.                  ")
    print("                                                 Rules                                               ")
    print("                        Regular counters can only move forward but only diagonally.                  ")
    print("                       King counters can move forward and backward but only diagonally.              ")


    try:
        htPlay = int(raw_input("Press 0 to Exit: "))
    except ValueError:
        print("You must enter an number.")

    if htPlay == 0:
        menu()
    else:
        print("Press 0 to Exit")

def menu():
    print("                    MENU                 ")
    print("           Player vs Player: Press 1     ")
    print("             How To Play: Press 2        ")
    print("                 Exit: Press 0           ")

    try:
        menuInput = int(raw_input("Pick From The Menu: "))
    except ValueError:
        print("You must enter an number.")

    if menuInput == 1:
        while True:
            blackMove(board)
            whoWins(board)
            whiteMove(board)
            whoWins(board)
    if menuInput == 2:
        htPlay()
    else:
        sys.exit()

while True:
    menu()
