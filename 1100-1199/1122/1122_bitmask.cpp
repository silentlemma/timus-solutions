#include <cstdio>
#include <vector>

const int SIZE = 4, PATTERN = 3, CELLS = SIZE * SIZE, ALL = (1 << CELLS) - 1;

int main() {
    char rows[SIZE][SIZE + 2], pattern[PATTERN][PATTERN + 2];
    for (auto &row : rows)
        if (scanf("%5s", row) != 1)
            return 0;
    for (auto &row : pattern)
        if (scanf("%4s", row) != 1)
            return 0;
    int board = 0;
    for (int r = 0; r < SIZE; r++)
        for (int c = 0; c < SIZE; c++)
            if (rows[r][c] == 'B')
                board |= 1 << (r * SIZE + c);
    // the flips of a move in each cell, the pattern clipped at the edges
    int moves[CELLS];
    for (int r = 0; r < SIZE; r++)
        for (int c = 0; c < SIZE; c++) {
            int mask = 0;
            for (int dr = 0; dr < PATTERN; dr++)
                for (int dc = 0; dc < PATTERN; dc++) {
                    int rr = r + dr - 1, cc = c + dc - 1;
                    if (pattern[dr][dc] == '1' && rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE)
                        mask |= 1 << (rr * SIZE + cc);
                }
            moves[r * SIZE + c] = mask;
        }
    // moves commute and a second move in a cell undoes the first, so a
    // solution is a set of cells; flips[s] is the effect of the set s
    std::vector<int> flips(1 << CELLS, 0);
    int best = -1;
    for (int s = 0; s < (1 << CELLS); s++) {
        if (s)
            flips[s] = flips[s & (s - 1)] ^ moves[__builtin_ctz(s)];
        if (flips[s] == board || flips[s] == (board ^ ALL)) {
            int count = __builtin_popcount(s);
            if (best < 0 || count < best)
                best = count;
        }
    }
    if (best < 0)
        puts("Impossible");
    else
        printf("%d\n", best);
}
