# Meta stuffs


def checkPawn(c1, r1, c2, r2, pieces):
    pass


def checkRook(c1, r1, c2, r2, pieces):
    pass


def checkKnight(c1, r1, c2, r2, pieces):
    pass


def checkBishop(c1, r1, c2, r2, pieces):
    pass


def checkQueen(c1, r1, c2, r2, pieces):
    pass


def checkKing(c1, r1, c2, r2, pieces):
    pass


def start(startSpot, endSpot, pieces):
    c1, r1 = startSpot
    c2, r2 = endSpot
    piece = pieces[c1][r1][1]
    if piece == "p":
        return checkPawn(c1, r1, c2, r2, pieces)
    elif piece == "r":
        return checkRook(c1, r1, c2, r2, pieces)
    elif piece == "n":
        return checkKnight(c1, r1, c2, r2, pieces)
    elif piece == "b":
        return checkBishop(c1, r1, c2, r2, pieces)
    elif piece == "q":
        return checkQueen(c1, r1, c2, r2, pieces)
    elif piece == "k":
        return checkKing(c1, r1, c2, r2, pieces)
    elif piece == "oo":
        return False
    else:
        raise RuntimeError('How did you fuck up this bad‽') from error
        return False
