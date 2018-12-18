# Comment for meta

import tkinter as tk
import os
import time
import rules

Width = Height = 600
# pieces = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
#           ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
#           ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
#           ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
#           ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
#           ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
#           ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
#           ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
# pieces = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],  # Pawns
#           ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
#           ['wp', 'oo', 'oo', 'oo', 'bp', 'oo', 'oo', 'wp'],
#           ['oo', 'oo', 'bp', 'wp', 'oo', 'oo', 'bp', 'oo'],
#           ['oo', 'oo', 'oo', 'oo', 'bp', 'oo', 'oo', 'bp'],
#           ['bp', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
#           ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
#           ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
# pieces = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],  # Knight
#           ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
#           ['wp', 'oo', 'oo', 'oo', 'bp', 'oo', 'oo', 'wp'],
#           ['oo', 'wn', 'bp', 'wp', 'bn', 'oo', 'bp', 'oo'],
#           ['oo', 'oo', 'oo', 'oo', 'bp', 'oo', 'oo', 'bp'],
#           ['bp', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
#           ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
#           ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
pieces = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],  # Rook
          ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
          ['wp', 'oo', 'oo', 'oo', 'bp', 'oo', 'oo', 'wp'],
          ['oo', 'wn', 'bp', 'br', 'bn', 'oo', 'bp', 'oo'],
          ['oo', 'oo', 'oo', 'oo', 'bp', 'oo', 'oo', 'bp'],
          ['bp', 'oo', 'wr', 'oo', 'oo', 'oo', 'oo', 'oo'],
          ['wp', 'wp', 'wp', 'wp', 'wp', 'wr', 'wp', 'wp'],
          ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
root = tk.Tk()
root.title('Chess Board')
root.resizable(False, False)
board = tk.Canvas(root, width=Width, height=Height)
imageList = []
board.pack()


def drawSquares():
    for SquareY in range(0, 8):
        for SquareX in range(0, 8):
            if (SquareX+SquareY) % 2 == 0:
                board.create_rectangle(1*SquareX*(Width/8),
                                       1*SquareY*(Height/8),
                                       (1*SquareX*(Width/8))+(Width/8),
                                       (1*SquareY*(Height/8))+(Height/8),
                                       fill='#EEEED2', outline='')
            else:
                board.create_rectangle(1*SquareX*(Width/8),
                                       1*SquareY*(Height/8),
                                       (1*SquareX*(Width/8))+(Width/8),
                                       (1*SquareY*(Height/8))+(Height/8),
                                       fill='#75955A', outline='')


def importPieces():
    for column in range(8):
        for row in range(8):
            if not pieces[column][row] == 'oo':
                imageList.append(((tk.PhotoImage(file=(os.getcwd() + "/chessIcons/" + pieces[column][row] + ".png"))).zoom(int(Width/8))).subsample(108))
                color = 'white' if str(pieces[column][row])[0] == 'w' else 'black'
                board.create_image(row*(Width/8), column*(Height/8),
                                   image=imageList[len(imageList)-1], anchor=tk.NW,
                                   tags=(imageList[len(imageList)-1], color))


def gameLoop(AI=False):
    DONE = gameEnd = clicked = False
    drawSquares()
    importPieces()
    while not DONE:
        if gameEnd:
            DONE = True
            print("The game has ended.")
            return
        elif AI:
            pass
        else:
            pass
        # print("here did " + str(clicked))

        def callback(event):
            print("clicked at", event.x, event.y)
            print(str(event.x // (Width/8)) + ", " + str(event.y // (Height/8)))
            start = ((event.x // (Width/8)), (event.y // (Height/8)))
            if rules.start(start, end, pieces):
                return
            else:
                return

        # x_root, y_root
        board.bind("<Button-1>", callback)
        root.update()
        time.sleep(0.1)


print(pieces)
gameLoop()
root.mainloop()
