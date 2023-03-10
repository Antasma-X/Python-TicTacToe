TicTacToe= [' ' for x in range(9)]

def printBoard():
    print(TicTacToe[0]+"  | "+TicTacToe[1]+" |  "+TicTacToe[2])
    print("-----------")
    print(TicTacToe[3]+"  | "+TicTacToe[4]+" |  "+TicTacToe[5])
    print("-----------")
    print(TicTacToe[6]+"  | "+TicTacToe[7]+" |  "+TicTacToe[8])

def placeUserOne():
    val=int(input("Place X:"))
    if TicTacToe[val]==' ':
        TicTacToe[val]="X"
    else:
        print("invalid")
        exit()


def placeUserTwo():
    val=int(input("Place O:"))
    if TicTacToe[val]==' ':
        TicTacToe[val]="O"
    else:
        print("invalid")
        exit()

def isBoardFull():
    checkWin()
    for i in range(9):
        if TicTacToe[i]=='X' or TicTacToe[i]=='X':
            pass
        else:
            return
    print("Draw")
    exit()
    

def isWinTwo():
    if TicTacToe[0]=='O' and TicTacToe[1]=='O' and TicTacToe[2]=='O'or TicTacToe[3]=='O' and TicTacToe[4]=='O' and TicTacToe[5]=='O' or TicTacToe[6]=='O' and TicTacToe[7]=='O' and TicTacToe[8]=='O' or TicTacToe[0]=='O' and TicTacToe[3]=='O' and TicTacToe[6]=='O'or TicTacToe[1]=='O' and TicTacToe[4]=='O' and TicTacToe[7]=='O' or TicTacToe[2]=='O' and TicTacToe[5]=='O' and TicTacToe[8]=='O' or TicTacToe[2]=='O' and TicTacToe[4]=='O' and TicTacToe[6]=='O'or TicTacToe[0]=='O' and TicTacToe[4]=='O' and TicTacToe[8]=='O':
        print("Player 2 wins!")
        exit()

def isWinOne():
    if TicTacToe[0]=='X' and TicTacToe[1]=='X' and TicTacToe[2]=='X'or TicTacToe[3]=='X' and TicTacToe[4]=='X' and TicTacToe[5]=='X' or TicTacToe[6]=='X' and TicTacToe[7]=='X' and TicTacToe[8]=='X' or TicTacToe[0]=='X' and TicTacToe[3]=='X' and TicTacToe[6]=='X'or TicTacToe[1]=='X' and TicTacToe[4]=='X' and TicTacToe[7]=='X' or TicTacToe[2]=='X' and TicTacToe[5]=='X' and TicTacToe[8]=='X' or TicTacToe[2]=='X' and TicTacToe[4]=='X' and TicTacToe[6]=='X'or TicTacToe[0]=='X' and TicTacToe[4]=='X' and TicTacToe[8]=='X':
        print("Player 1 wins!")
        exit()

def checkWin():
    isWinOne()
    isWinTwo()


def play():
    print("Lets play Tic Tac Toe")
    gameIsPlaying=True
    printBoard()
    while gameIsPlaying==True:
        placeUserOne()
        printBoard()
        checkWin()
        isBoardFull()
        placeUserTwo()
        printBoard()
        checkWin()
        isBoardFull()

play()