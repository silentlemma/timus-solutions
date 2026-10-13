#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>

using namespace std;

const int BITS = 21; // the answer stays below 900 000 cells, a table of 2^21 is enough
const int WORD = 64;
const int SLOTS = 1 << BITS;
const unsigned long long MIX = 0x9E3779B97F4A7C15ULL;

// an open-addressing set of cell numbers; 0 marks an empty slot, so numbers are stored + 1
vector<unsigned long long> table(SLOTS, 0);
int distinctCells = 0;

void add(unsigned long long cell) {
    unsigned long long key = cell + 1;
    size_t h = (key * MIX) >> (WORD - BITS);
    while (table[h] != 0 && table[h] != key)
        h = (h + 1) & (SLOTS - 1);
    if (table[h] == 0) {
        table[h] = key;
        distinctCells++;
    }
}

int n, s;

// how many steps fit on the board from cell in direction v
int room(const vector<int> &cell, const vector<int> &v) {
    int r = s;
    for (int i = 0; i < n; i++)
        if (v[i] != 0)
            r = min(r, v[i] > 0 ? s - 1 - cell[i] : cell[i]);
    return r;
}

int main() {
    scanf("%d %d", &n, &s);
    vector<int> start(n);
    for (int &c : start) {
        scanf("%d", &c);
        c--;
    }
    // a cell is the number with digits x_i in base S
    vector<long long> weight(n, 1);
    for (int i = 1; i < n; i++)
        weight[i] = weight[i - 1] * s;
    // rook directions along each axis, bishop directions along all axes at once
    set<vector<int>> dirSet;
    for (int i = 0; i < n; i++)
        for (int sign : {1, -1}) {
            vector<int> v(n, 0);
            v[i] = sign;
            dirSet.insert(v);
        }
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> v(n);
        for (int i = 0; i < n; i++)
            v[i] = (mask >> i & 1) ? -1 : 1;
        dirSet.insert(v); // in one dimension they coincide with the rook ones
    }
    vector<vector<int>> dirs(dirSet.begin(), dirSet.end());
    set<vector<int>> first;
    for (auto &v : dirs)
        for (int k = 1, r = room(start, v); k <= r; k++) {
            vector<int> cell(n);
            for (int i = 0; i < n; i++)
                cell[i] = start[i] + k * v[i];
            first.insert(cell);
        }
    for (auto &cell : first) {
        long long here = 0;
        for (int i = 0; i < n; i++)
            here += cell[i] * weight[i];
        for (auto &v : dirs) {
            long long step = 0;
            for (int i = 0; i < n; i++)
                step += v[i] * weight[i];
            // every cell on the ray after the first move
            for (int k = 1, r = room(cell, v); k <= r; k++)
                add(here + k * step);
        }
    }
    printf("%d\n", distinctCells);
}
