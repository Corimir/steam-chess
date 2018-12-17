# Comment for meta

import tkinter as tk
import os

Width = Height = 50
pieces = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
          ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
          ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
          ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
          ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
          ['oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo', 'oo'],
          ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
          ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
root = tk.Tk()
root.title('Chess Board')
root.resizable(False, False)
board = tk.Canvas(root, width=Width, height=Height)
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
    for i in range(len(pieces)):
        for t in range(len(pieces[i])):
            if not pieces[i][t] == 'oo':
                    pieces[i][t] = tk.PhotoImage(file=(os.getcwd() +
                                                 "/chessIcons/" +
                                                 pieces[i][t] + ".png"))
                    pieces[i][t] = pieces[i][t].zoom(int(Width/8))
                    pieces[i][t] = pieces[i][t].subsample(108)
                    board.create_image(t*(Width/8), i*(Height/8),
                                       image=pieces[i][t], anchor=tk.NW,
                                       tags=pieces[i][t])


drawSquares()
importPieces()
root.mainloop()
