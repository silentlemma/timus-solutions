#include <cstdio>

const int LIMIT = 10000, INPUT_FIELDS = 3;
unsigned char shapes[LIMIT + 1];

int main() {
    int before, after, added;
    if (scanf("%d%d%d", &before, &after, &added) != INPUT_FIELDS)
        return 0;
    // Each unordered divisor pair has a unique smaller side.
    for (int side = 1; side * side <= LIMIT; side++)
        for (int tiles = side * side; tiles <= LIMIT; tiles += side)
            shapes[tiles]++;
    for (int tiles = added + 1; tiles <= LIMIT; tiles++)
        if (shapes[tiles] == after && shapes[tiles - added] == before) {
            printf("%d\n", tiles);
            return 0;
        }
    puts("0");
}
