#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n * n + n / 2 + 1);
    // a chessboard: the large numbers go down on one colour and the small
    // ones up on the other, both in reading order
    int big = n * n, small = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            printf("%d%c", (i + j) % 2 == 0 ? big-- : small++, j + 1 < n ? ' ' : '\n');
}
