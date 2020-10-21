#this module creates the AI for making and deciding moves
import random
from functions import *



def compMove():
    possiblemoves = []
    idx = 0
    for i in board:
        if i == " ":
            possiblemoves.append(idx)
        idx = idx + 1

    for i in possiblemoves:
        boardcopy = board.copy()
        enterBoardIDX(i, "O", boardcopy)
        if checkWin("O", boardcopy) == True:
            return i

    for i in possiblemoves:
        boardcopy = board.copy()
        enterBoardIDX(i, "X", boardcopy)
        if checkWin("X", boardcopy) == True:
            return i


    if 4 in possiblemoves:
        return 4

    if 0 in possiblemoves:
        return 0

    if 2 in possiblemoves:
        return 2

    if 6 in possiblemoves:
        return 6

    if 8 in possiblemoves:
        return 8

    return random.choice(possiblemoves)




