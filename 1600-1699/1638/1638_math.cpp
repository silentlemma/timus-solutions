#include <cstdio>

int main() {
    int pages, cover, start, stop;
    if (scanf("%d %d", &pages, &cover) != 2 || scanf("%d %d", &start, &stop) != 2)
        return 0;
    // on a shelf a volume's first page faces its right neighbour and its
    // last page faces the left one
    int whole = pages + 2 * cover, length;
    if (start == stop)
        length = pages;
    else if (start < stop)
        length = 2 * cover + (stop - start - 1) * whole;
    else
        length = 2 * pages + 2 * cover + (start - stop - 1) * whole;
    printf("%d\n", length);
}
