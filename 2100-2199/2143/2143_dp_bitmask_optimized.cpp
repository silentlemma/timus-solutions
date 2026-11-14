#include <array>
#include <cstdint>
#include <cstdio>

constexpr int MAX_ROWS = 100;
constexpr int SIDE = 3;
constexpr int RIGHT_START = 6;
constexpr int ROW_BUFFER = 10;
constexpr int UNREACHABLE = -MAX_ROWS * SIDE;
constexpr int STATES = 5;
constexpr std::array<int, STATES> MASKS{0, 1, 2, 1 << 2, 1 | (1 << 2)};
constexpr std::array<int, MASKS.size()> PEOPLE{0, 1, 1, 1, 2};

using Rows = std::array<std::array<int, MAX_ROWS>, 2>;

int arrange(std::array<int, MAX_ROWS> &rows, int n) {
    std::array<std::array<uint8_t, MASKS.size()>, MAX_ROWS> previous{};
    std::array<int, MASKS.size()> scores;
    scores.fill(UNREACHABLE);
    scores[0] = 0;
    for (int row = 0; row < n; ++row) {
        std::array<int, MASKS.size()> next;
        next.fill(UNREACHABLE);
        for (size_t state = 0; state < MASKS.size(); ++state) {
            const int mask = MASKS[state];
            if ((mask & rows[row]) != mask)
                continue;
            const int blocked = mask | (mask << 1) | (mask >> 1);
            for (size_t last = 0; last < MASKS.size(); ++last) {
                if ((blocked & MASKS[last]) == 0 && scores[last] > next[state]) {
                    next[state] = scores[last];
                    previous[row][state] = static_cast<uint8_t>(last);
                }
            }
            next[state] += PEOPLE[state];
        }
        scores = next;
    }
    size_t state = 0;
    for (size_t i = 1; i < MASKS.size(); ++i)
        if (scores[i] > scores[state])
            state = i;
    const int count = scores[state];
    for (int row = n - 1; row >= 0; --row) {
        rows[row] = MASKS[state];
        state = previous[row][state];
    }
    return count;
}

int main() {
    int n, group;
    if (scanf("%d %d", &n, &group) != 2)
        return 0;
    Rows rows{};
    for (int row = 0; row < n; ++row) {
        char line[ROW_BUFFER];
        if (scanf("%9s", line) != 1)
            return 0;
        for (int side = 0; side < 2; ++side)
            for (int column = 0; column < SIDE; ++column)
                if (line[side * RIGHT_START + column] == '.')
                    rows[side][row] |= 1 << column;
    }
    int total = arrange(rows[0], n) + arrange(rows[1], n);
    if (total < group) {
        puts("PORAZHENIE");
        return 0;
    }
    puts("POBEDA");
    for (int row = 0; row < n && group > 0; ++row)
        for (int side = 0; side < 2 && group > 0; ++side)
            for (int column = 0; column < SIDE && group > 0; ++column)
                if ((rows[side][row] & (1 << column)) != 0) {
                    printf("%d%c\n", row + 1, 'A' + side * SIDE + column);
                    --group;
                }
}
