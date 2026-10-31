#include <algorithm>
#include <cstdio>
constexpr int MAX_PIGEONS = 100;
constexpr int STEP = 5; // four characters of a pigeon and a separating column
// each row has 5*n-1 non-space characters, plus its terminating zero.
constexpr int ROW_SIZE = STEP * MAX_PIGEONS;
constexpr int FORMAT_SIZE = 16; // "%", the digits of the width, "s" and the terminating zero
int main() {
    // the scanf format of a row: width ROW_SIZE - 1 leaves room for the terminating zero
    char row_format[FORMAT_SIZE];
    snprintf(row_format, sizeof row_format, "%%%ds", ROW_SIZE - 1);
    int n;
    scanf("%d", &n);
    char row[ROW_SIZE];
    scanf(row_format, row);
    // halves counts the pigeons that break the pattern with the left half looking
    // left, parity those that break the pattern with even positions looking left,
    // and the two opposite patterns break exactly at the other pigeons
    int halves = 0, parity = 0;
    for (int i = 0; i < n; ++i) {
        bool left = row[i * STEP] == '<';
        halves += left != (i < n / 2);
        parity += left != (i % 2 == 0);
    }
    // the remaining rows carry no orientation information, but are still consumed.
    scanf(row_format, row);
    scanf(row_format, row);
    printf("%d\n", std::min({halves, n - halves, parity, n - parity}));
}
