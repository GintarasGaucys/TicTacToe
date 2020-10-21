from ai import *
from functions import *

#Prints the board list
def printBoard():
    print("   |   |    ")
    print(" " +board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("   |   |    ")
    print("------------")
    print("   |   |    ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("   |   |    ")
    print("------------")
    print("   |   |    ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("   |   |    ")
    print("\n")




done = False
moves = 0
tie = False
while not done:
    printBoard()
    print("YOU ARE X")
    print("The correct format to enter a move is row, column. Example: '1 2' would put an x on the second square")
    while checkWin("O", board) == False and checkWin("X", board) == False:
        try:
            answer = tuple(map(int, input("\n").split(' ')))
            enterBoard(answer, "X")
        except:
            print("Incorrect input.")
            break
        if " " not in board:
            tie = True
            break
        enterBoardIDX(compMove(), "O", board)
        printBoard()


    if checkWin("X", board) == True:
        print("You won!\n")

    elif checkWin("O", board) == True:
        print("You lost!\n")
    elif tie:
        printBoard()
        print("Tie!")

    done = True




