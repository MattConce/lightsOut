#define MAX 200
#define TRUE 1
#define FALSE 0



enum State
{
  on,
  off
};

typedef unsigned int Bool;

typedef struct pixel Pixel;
struct pixel
{
  int row, col;
  int state;
};

typedef struct board Board;
struct board
{
  int width, height;
  Pixel **pixel;
};

/* Prototypes */

Board* createBoard(int, int);

void printBoard(Board*, int, int);
