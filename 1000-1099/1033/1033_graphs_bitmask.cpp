#include <cstdint>
#include <cstdio>

const int MAX_SIDE = 33, SIDE_AREA = 9, ENTRANCE_SIDES = 4;
uint64_t open_rows[MAX_SIDE], seen[MAX_SIDE], front[MAX_SIDE];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    char row[MAX_SIDE + 1];
    for (int r = 0; r < n; r++) {
        if (scanf("%33s", row) != 1)
            return 0;
        for (int c = 0; c < n; c++)
            if (row[c] == '.')
                open_rows[r] |= uint64_t(1) << c;
    }
    seen[0] = front[0] = 1;
    seen[n - 1] = front[n - 1] = uint64_t(1) << (n - 1);
    uint64_t active = 1 | (uint64_t(1) << (n - 1));
    // One row event consumes only newly reached cells; masks batch neighbours.
    // Mark on enqueue, so every cell enters a frontier exactly once.
    while (active) {
        int r = __builtin_ctzll(active);
        active &= active - 1;
        uint64_t cells = front[r];
        front[r] = 0;
        for (int q = r - 1; q <= r + 1; q++) {
            if (q < 0 || q >= n)
                continue;
            uint64_t next = q == r ? (cells << 1) | (cells >> 1) : cells;
            next &= open_rows[q] & ~seen[q];
            if (next) {
                seen[q] |= next;
                front[q] |= next;
                active |= uint64_t(1) << q;
            }
        }
    }
    int sides = 0;
    for (int r = 0; r < n; r++) {
        sides += __builtin_popcountll(seen[r] & ~(open_rows[r] << 1));
        sides += __builtin_popcountll(seen[r] & ~(open_rows[r] >> 1));
        sides += __builtin_popcountll(seen[r] & ~(r ? open_rows[r - 1] : 0));
        sides += __builtin_popcountll(seen[r] & ~(r + 1 < n ? open_rows[r + 1] : 0));
    }
    printf("%d\n", (sides - ENTRANCE_SIDES) * SIDE_AREA);
}
