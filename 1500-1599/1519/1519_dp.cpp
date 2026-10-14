#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

typedef uint64_t u64;
const u64 OPEN = 1, CLOSE = 2; // the ends of a path piece, matched like brackets
const u64 FLIP = OPEN ^ CLOSE; // turns one end into the other
const int BITS = 2;            // bits per plug
const u64 MASK = 3;

// the plug matching the bracket at pos, searching towards step
int partner(u64 state, int pos, int step) {
    for (int depth = 0;; pos += step) {
        u64 v = state >> (BITS * pos) & MASK;
        if (v == OPEN)
            depth += step;
        else if (v == CLOSE)
            depth -= step;
        if (depth == 0)
            return pos;
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> free(n + 1, vector<bool>(m + 1, false));
    int last = 0;
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < m; j++)
            if (row[j] == '.') {
                free[i][j] = true;
                last = i * m + j;
            }
    }
    // a state holds m + 1 plugs: plug j is the left side of the current cell
    // when j is its column, plug j + 1 its upper side; the rest are the lower
    // sides of the row above or this row
    unordered_map<u64, u64> ways = {{0, 1}};
    u64 total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            unordered_map<u64, u64> next;
            next.reserve(ways.size() * 2);
            int sl = BITS * j, su = BITS * (j + 1);
            u64 clear = ~(MASK << sl) & ~(MASK << su);
            bool down = free[i + 1][j], right = free[i][j + 1];
            for (auto [state, count] : ways) {
                u64 left = state >> sl & MASK, up = state >> su & MASK, base = state & clear;
                if (!free[i][j]) {
                    if (left == 0 && up == 0)
                        next[state] += count;
                } else if (left == 0 && up == 0) {
                    if (down && right)
                        next[base | OPEN << sl | CLOSE << su] += count;
                } else if (left == 0 || up == 0) {
                    u64 end = left | up;
                    if (down)
                        next[base | end << sl] += count;
                    if (right)
                        next[base | end << su] += count;
                } else if (left == up) {
                    // two openings or two closings: the far end of one of the
                    // joined pieces changes its kind
                    int far = left == OPEN ? partner(state, j + 1, 1) : partner(state, j, -1);
                    next[base ^ FLIP << (BITS * far)] += count;
                } else if (left == CLOSE) {
                    next[base] += count;
                } else if (i * m + j == last && base == 0) {
                    total += count; // the loop closes on the last free cell
                }
            }
            ways.swap(next);
        }
        // the next row starts with an empty left plug
        unordered_map<u64, u64> shifted;
        for (auto [state, count] : ways)
            shifted[state << BITS] += count;
        ways.swap(shifted);
    }
    cout << total << "\n";
}
