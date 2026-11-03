#include <algorithm>
#include <cstdio>
#include <unordered_map>

const int SIZE = 4, PATTERN = 3, CELLS = SIZE * SIZE, ALL = (1 << CELLS) - 1;

const int HALF = CELLS / 2;

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
    // Split the commuting moves in half and match their XOR effects.
    // Duplicate left effects retain only the cheapest number of moves.
    std::unordered_map<int, int> left;
    left.reserve(1 << HALF);
    int effect = 0;
    for (int step = 0; step < (1 << HALF); step++) {
        if (step)
            effect ^= moves[__builtin_ctz(step)];
        int count = __builtin_popcount(step ^ (step >> 1));
        auto found = left.find(effect);
        if (found == left.end() || count < found->second)
            left[effect] = count;
    }
    int best = CELLS + 1;
    effect = 0;
    for (int step = 0; step < (1 << HALF); step++) {
        if (step)
            effect ^= moves[HALF + __builtin_ctz(step)];
        int count = __builtin_popcount(step ^ (step >> 1));
        for (int target : {board ^ effect, board ^ ALL ^ effect}) {
            auto found = left.find(target);
            if (found != left.end())
                best = std::min(best, count + found->second);
        }
    }
    if (best > CELLS)
        puts("Impossible");
    else
        printf("%d\n", best);
}
