# Comment for meta

import tkinter as tk
import os

Width = Height = 60
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
    for column in range(8):
        for row in range(8):
            if not pieces[column][row] == 'oo':
                # ((tk.PhotoImage(file=(os.getcwd() + "/chessIcons/" +
                # pieces[column][row] + ".png"))).zoom(int(Width/8)))
                # .subsample(108)
                # pieces[column][row] = pieces[column][row].zoom(int(Width/8))
                # pieces[column][row] = pieces[column][row].subsample(108)
                board.create_image(row*(Width/8), column*(Height/8),
                                   image=((tk.PhotoImage(file=(os.getcwd() + "/chessIcons/" + pieces[column][row] + ".png"))).zoom(int(Width/8))).subsample(108), anchor=tk.NW,
                                   tags=((tk.PhotoImage(file=(os.getcwd() + "/chessIcons/" + pieces[column][row] + ".png"))).zoom(int(Width/8))).subsample(108))


drawSquares()
importPieces()
print(pieces)
root.mainloop()
