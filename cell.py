import pygame as pg

class cell:
    def __init__(s, i, j, l, W, H):
        s.cor = (0, 0, 0)
        s.cx, s.cy = convert(i,j,l,W,H)
        s.state = False
        s.w, s.h, s.i, s.j = W, H, i, j


        r = l/2
        s.vertex = (
          (s.cx-r, s.cy-r),
          (s.cx+r, s.cy-r),
          (s.cx+r, s.cy+r),
          (s.cx-r, s.cy+r)
        )
    def draw(s, src):
        if s.state:
            s.cor = (10, 200, 50)
        else:
            s.cor = (0, 0, 0)

        pg.draw.polygon(src, s.cor, s.vertex, 0)
        pg.draw.lines(src, (255,255,255), True, s.vertex, 1)

    def toggling(s, board):
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = s.i + i
                col = s.j + j
                if inGrid(row, col, s.w, s.h) and ((abs(i)+abs(j)) != 2):
                    board[row][col].state = not board[row][col].state


def convert(i, j, l, W, H):
    # print(f'i = {i:d}, j = {j:d}')
    y, x = (i*l+l/2), (j*l+l/2)
    # print(f'x = {x:f}, y = {y:f}\n')
    return x, y

def inGrid(i, j, w, h):
    return i >= 0 and i <= h-1 and j >= 0 and j <= w-1
