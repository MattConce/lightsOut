#include <stdlib.h>
#include <stdio.h>  /* fprintf() */
#include "board.h"
#define board(i, j) board->pixel[i][j]


/* Functions */

Board* createBoard(int w, int h)
{
  Board *board = malloc(sizeof(Board));
  board->pixel = malloc(h * sizeof(Pixel*));
  for (int i = 0; i < h; i++) {
    board->pixel[i] = malloc(w * sizeof(Pixel));
  }
  board->width = w;
  board->height = h;
  for (int row = 0; row < h; row++) {
    for (int col = 0; col < w; col++) {
      board(row, col).row = row;
      board(row, col).col = col;
      board(row, col).state = FALSE;
    }
  }
  return board;
}

void printBoard(Board *board, int w, int h)
{
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      printf(" %d ", board(i, j).state);
    }
    printf("\n");
  }
}
