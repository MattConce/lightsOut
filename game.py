import pygame as pg
import random as rd
from cell import cell
# import pygameMenu as pm              # This imports classes and other things
# from pm.locals import*  # Import constants (like actions)


def randlightsOutGrid(W, H, l):
    board = []
    for i in range(H):
        board.append([])
        for j in range(W):
            board[i].append(cell(i, j, l, W, H))

    n = H * W
    low, high = 0.55*n, 0.85*n
    d = float(rd.randint(0,3000)/3000+1)
    k = d * (high-low+1)
    k = low + k
    for p in range(n):
        i, j = rd.randint(0,H-1), rd.randint(0,W-1)
        board[i][j].toggling(board)

    return board




def main():
    #
    H, W, M, l = 5, 5, 1, 100

    # Initialize pygame
    pg.init()
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [H*l+M, W*l+M]
    src = pg.display.set_mode(WINDOW_SIZE)
    # pm.Menu(src, H, W, font, "Lights Out!", *args)
    # Set the board
    board = randlightsOutGrid(W, H, l)
    # Set a title for the screen
    pg.display.set_caption("Lights Out!")
    # Loop until the user clicks the close button
    done=False
    # Used to manage how fast the screen updates
    clock = pg.time.Clock()

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=True
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                col, row = pos[0]//l, pos[1]//l
                board[row][col].toggling(board)

        # Clean screen
        src.fill((255,255,255))

        for i in range(H):
            for j in range(W):
                board[i][j].draw(src)

        clock.tick(60)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
