#include <cstdio>

const int LETTERS = 26, MAX_CELLS = 100, INPUT_FIELDS = 3;

int main() {
    int rows, columns, words;
    if (scanf("%d%d%d", &rows, &columns, &words) != INPUT_FIELDS)
        return 0;
    int left[LETTERS] = {};
    char token[MAX_CELLS + 1];
    // Disjoint embedded words remove exactly their letter multisets.
    for (int i = 0; i < rows + words; i++) {
        if (scanf("%100s", token) != 1)
            return 0;
        for (const char *p = token; *p; p++)
            left[*p - 'A'] += i < rows ? 1 : -1;
    }
    for (int c = 0; c < LETTERS; c++)
        for (int count = 0; count < left[c]; count++)
            putchar('A' + c);
    putchar('\n');
}
