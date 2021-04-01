CC=	gcc
CFLAGS=	-Wall -g -std=gnu99

all:	palindrome

palindrome:	palindrome.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f palindrome
