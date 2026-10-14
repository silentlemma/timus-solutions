#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const int SIZE = 8;

vector<pair<int, int>> jumps[SIZE * SIZE]; // (jumped square, landing square)
int total, best;

// black, white: the pieces still on the board, the mover excluded; removed:
// the white pieces taken away so far, taken: the blacks captured so far
void dfs(int square, uint64_t black, uint64_t white, int removed, int taken) {
    best = min(best, removed + total - taken); // every black not captured is taken away
    for (auto [mid, to] : jumps[square]) {
        if (!(black >> mid & 1))
            continue;
        uint64_t nb = black & ~(1ULL << mid), nw = white;
        int cost = removed;
        nb &= ~(1ULL << to); // a black in the way is taken away, uncaptured
        if (nw >> to & 1) {
            nw &= ~(1ULL << to); // a white in the way costs one more
            cost++;
        }
        dfs(to, nb, nw, cost, taken + 1);
    }
}

int main() {
    // square (x, y), both from 0, is bit x * SIZE + y; the first input line is y = 7
    uint64_t whites = 0, blacks = 0;
    for (int r = 0; r < SIZE; r++) {
        string line;
        cin >> line;
        for (int x = 0; x < SIZE; x++) {
            uint64_t bit = 1ULL << (x * SIZE + SIZE - 1 - r);
            if (line[x] == 'W')
                whites |= bit;
            else if (line[x] == 'B')
                blacks |= bit;
        }
    }
    // only squares off the edge can be jumped, so the landing stays on the board
    for (int x = 0; x < SIZE; x++)
        for (int y = 0; y < SIZE; y++)
            for (int dx = -1; dx <= 1; dx += 2)
                for (int dy = -1; dy <= 1; dy += 2) {
                    int tx = x + 2 * dx, ty = y + 2 * dy;
                    if (tx >= 0 && tx < SIZE && ty >= 0 && ty < SIZE)
                        jumps[x * SIZE + y].push_back({(x + dx) * SIZE + y + dy, tx * SIZE + ty});
                }
    total = best = __builtin_popcountll(blacks); // removing every black always wins
    for (int s = 0; s < SIZE * SIZE; s++)
        if (whites >> s & 1)
            dfs(s, blacks, whites & ~(1ULL << s), 0, 0);
    cout << best << "\n";
}
