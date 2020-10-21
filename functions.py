
enterboard = {(1, 1): 0, (1, 2): 1, (1, 3):2, (2, 1): 3, (2, 2):4, (2, 3):5, (3, 1):6, (3, 2):7, (3, 3):8}
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


#Checks for win of sym and returns True or False
def checkWin(sym, theboard=board):
    if theboard[4] == sym:
        if theboard[0] == sym and theboard[8] == sym:
            return True
        elif theboard[2] == sym and theboard[6] == sym:
            return True
        elif theboard[1] == sym and theboard[7] == sym:
            return True
        elif theboard[3] == sym and theboard[5] == sym:
            return True
    if theboard[0] == sym:
        if theboard[1] == sym and theboard[2] == sym:
            return True
        elif theboard[3] == sym and theboard[6] == sym:
            return True
    if theboard[2] == sym and board[5] == sym and theboard[8] == sym:
        return True
    if theboard[6] == sym and theboard[7] == sym and theboard[8] == sym:
        return True
    return False


#Enters a symbol (sym) in position (pos) in board list. Expects a tuple.
def enterBoard(pos, sym, theboard=board):
    if theboard[enterboard[pos]] == " ":
        theboard[enterboard[pos]] = sym


def enterBoardIDX(idx, sym, theboard=board):
    if theboard[idx] == " ":
        theboard[idx] = sym