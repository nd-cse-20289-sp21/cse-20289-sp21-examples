/* point.c */

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

void point_format(Point *p, FILE *stream) {
    fprintf(stream, "Point{x: %d, y: %d}\n", p->x, p->y);
}

int main(int argc, char *argv[]) {
    Point p0 = {0};
    Point p1 = {1, 2};

    printf("sizeof(Point) = %ld\n", sizeof(Point));

    point_format(&p0, stdout);
    point_format(&p1, stdout);

    Point pa[] = {
	{3, 4},
	{5, 6},
	{0},
    };

    for (Point *p = pa; p->x && p->y; p++) {
    	point_format(p, stdout);
    }

    return EXIT_SUCCESS;
}
