CC			=	gcc
CFLAGS 	=	-Wall -pedantic -std=c11 -O3 -g
RM     	= rm -f

lighstOut:	game.o	board.o
	$(CC)	game.o	board.o	-o	lighstOut	-lm

game.o:	game.c	board.h
	$(CC)	$(CFLAGS)	-c	game.c

board.o:	board.c	board.h
	$(CC) $(CFLAGS)	-c board.c

clean:
	$(RM) *.o *~ lighstOut

run:
	./lighstOut	3
