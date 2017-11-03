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

    newCounterBX = input("BLACK - Input the X coordinate for the place you want to move")
    newCounterBY = input("BLACK - Input the Y coordinate for the place you want to move")
    # if board[newCounterBX][newCounterBY] == '*':
    #     board[newCounterBX][newCounterBY] = 'B'
    # else:
    #     print("Cannot move here!")
    if board[newCounterBX][newCounterBY] == board[counterPlaceBX][counterPlaceBY]:
        print ("Cannot Move Here Invalid")
        continue
    else:
        board[newCounterBX][newCounterBY] == '*'
        board[newCounterBX][newCounterBY] = 'B'

    for rows in board:
        print rows
    break


# while True:
#     counterPlaceW1 = input("WHITE - Input the first coordinate ")
#     counterPlaceW2 = input("WHITE - Input the first coordinate ")
#     #counterPlaceSplit = counterPlace.split(',')
#     if board[counterPlaceW1][counterPlaceW2] == "W":
#         board[counterPlaceW1][counterPlaceW2] = '*'
#     else:
#         print("Not your counter")
#         continue
#     #print board[counterPlace1][counterPlace2]
#     for rows in board:
#         print rows
#     break
    #board(tuple(counterPlaceSplit))
#np.board(counterPlaceSplit)


#newPlace = input("Input the CoOrdinates of the place you want to move to: ")

#newPlaceSplit = newPlace.split(',')


#print(board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|"+board[0][3]+"|"+board[0][4]+"|"+board[0][5]+"|"+board[0][6]+"|"+board[0][7])
#print(board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|"+board[1][3]+"|"+board[1][4]+"|"+board[1][5]+"|"+board[1][6]+"|"+board[1][7])
#print(board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|"+board[2][3]+"|"+board[2][4]+"|"+board[2][5]+"|"+board[2][6]+"|"+board[2][7])
#print(board[3][0]+"|"+board[3][1]+"|"+board[3][2]+"|"+board[3][3]+"|"+board[3][4]+"|"+board[3][5]+"|"+board[3][6]+"|"+board[3][7])
#print(board[4][0]+"|"+board[4][1]+"|"+board[4][2]+"|"+board[4][3]+"|"+board[4][4]+"|"+board[4][5]+"|"+board[4][6]+"|"+board[4][7])
#print(board[5][0]+"|"+board[5][1]+"|"+board[5][2]+"|"+board[5][3]+"|"+board[5][4]+"|"+board[5][5]+"|"+board[5][6]+"|"+board[5][7])
#print(board[6][0]+"|"+board[6][1]+"|"+board[6][2]+"|"+board[6][3]+"|"+board[6][4]+"|"+board[6][5]+"|"+board[6][6]+"|"+board[6][7])
#print(board[7][0]+"|"+board[7][1]+"|"+board[7][2]+"|"+board[7][3]+"|"+board[7][4]+"|"+board[7][5]+"|"+board[7][6]+"|"+board[7][7])


#counterPlaceSplit = counterPlace.split(',')
#newPlaceSplit = newPlace.split(',')

#print counterPlaceSplit
#print newPlaceSplit
