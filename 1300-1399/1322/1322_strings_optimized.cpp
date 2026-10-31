#include <cstdio>

const int MAX_LENGTH = 100000, CHARS = 128, CHAR_BITS = 7;
char last[MAX_LENGTH + 1];
// seven low bits hold an ascii character; the remaining bits hold an index below 100000.
unsigned int order[MAX_LENGTH];
int start[CHARS + 1];
int main() {
    int k;
    if (scanf("%d %100000s", &k, last) != 2)
        return 0;
    // a stable counting sort of the last column: the row packed in order[j] ends
    // with the j-th character of the sorted column, the first one of row j
    int n = 0;
    while (last[n])
        start[static_cast<unsigned char>(last[n++]) + 1]++;
    for (int c = 0; c < CHARS; c++)
        start[c + 1] += start[c];
    for (int i = 0; i < n; i++) {
        unsigned int c = static_cast<unsigned char>(last[i]);
        order[start[c]++] = (static_cast<unsigned int>(i) << CHAR_BITS) | c;
    }
    int row = k - 1;
    for (int i = 0; i < n; i++) {
        unsigned int entry = order[row];
        putchar(entry & (CHARS - 1));
        row = entry >> CHAR_BITS;
    }
    putchar('\n');
}
