#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

constexpr int SIDE = 3;  // seats on each side of the aisle
constexpr int MASKS = 1 << SIDE;
constexpr int RIGHT_START = 6;  // the right seats in a row description
const char *LETTERS = "ABCDEF";

int n, k;
std::vector<std::string> rows;

// The largest set of free, pairwise non-adjacent seats on one side, as a
// mask per row; neighbours in a row and in the next row may not share a column
// or stand next to each other.
std::vector<int> bestSide(int offset) {
    std::vector<std::vector<int>> best(n + 1, std::vector<int>(MASKS, -1));
    std::vector<std::vector<int>> from(n + 1, std::vector<int>(MASKS, 0));
    best[0][0] = 0;
    for (int r = 0; r < n; r++) {
        int freeMask = 0;
        for (int s = 0; s < SIDE; s++)
            if (rows[r][offset + s] == '.') freeMask |= 1 << s;
        for (int cur = 0; cur < MASKS; cur++) {
            if ((cur & ~freeMask) || (cur & (cur << 1))) continue;
            int count = __builtin_popcount(cur);
            for (int prev = 0; prev < MASKS; prev++) {
                if (best[r][prev] < 0) continue;
                if ((prev | prev << 1 | prev >> 1) & cur) continue;
                if (best[r][prev] + count > best[r + 1][cur]) {
                    best[r + 1][cur] = best[r][prev] + count;
                    from[r + 1][cur] = prev;
                }
            }
        }
    }
    int mask = 0;
    for (int m = 0; m < MASKS; m++)
        if (best[n][m] > best[n][mask]) mask = m;
    std::vector<int> chosen(n);
    for (int r = n; r > 0; r--) {
        chosen[r - 1] = mask;
        mask = from[r][mask];
    }
    return chosen;
}

int main() {
    std::cin >> n >> k;
    rows.resize(n);
    for (auto &row : rows) std::cin >> row;
    std::vector<std::string> seats;
    for (int side = 0; side < 2; side++) {
        std::vector<int> chosen = bestSide(side * RIGHT_START);
        for (int r = 0; r < n; r++)
            for (int s = 0; s < SIDE; s++)
                if (chosen[r] >> s & 1)
                    seats.push_back(std::to_string(r + 1) + LETTERS[side * SIDE + s]);
    }
    if ((int)seats.size() < k) {
        puts("PORAZHENIE");
        return 0;
    }
    puts("POBEDA");
    for (int i = 0; i < k; i++) puts(seats[i].c_str());
    return 0;
}
