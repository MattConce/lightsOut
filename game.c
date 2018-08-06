#include <stdio.h>  /* fprintf() */
#include <stdlib.h> /* exit(), EXIT_FAILURE  */
#include "board.h"

int main(int argc, char** argv)
{
  int n = atoi(argv[1]);

  Board *board = createBoard(n, n);
  // initGame();
  printBoard(board, n, n);

}
