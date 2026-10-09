#include <cstdio>

const int SIZE = 4, CELLS = SIZE * SIZE;

int main() {
    // the board as 16 bits, bit r * 4 + c set for a black piece
    int board = 0;
    for (int r = 0; r < SIZE; r++) {
        char row[SIZE + 1];
        if (scanf("%4s", row) != 1)
            return 0;
        for (int c = 0; c < SIZE; c++)
            if (row[c] == 'b')
                board |= 1 << (r * SIZE + c);
    }
    // the pieces turned by a move at each cell
    int move[CELLS];
    const int dr[] = {0, 1, -1, 0, 0}, dc[] = {0, 0, 0, 1, -1};
    for (int r = 0; r < SIZE; r++)
        for (int c = 0; c < SIZE; c++) {
            int m = 0;
            for (size_t d = 0; d < sizeof dr / sizeof dr[0]; d++) {
                int rr = r + dr[d], cc = c + dc[d];
                if (rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE)
                    m |= 1 << (rr * SIZE + cc);
            }
            move[r * SIZE + c] = m;
        }
    // moves commute and a move made twice cancels, so a solution is a set of
    // cells: try all 2^16 sets
    const int all = (1 << CELLS) - 1;
    int best = -1;
    for (int set = 0; set <= all; set++) {
        int b = board, count = 0;
        for (int i = 0; i < CELLS; i++)
            if (set >> i & 1) {
                b ^= move[i];
                count++;
            }
        if ((b == 0 || b == all) && (best < 0 || count < best))
            best = count;
    }
    if (best < 0)
        printf("Impossible\n");
    else
        printf("%d\n", best);
}
