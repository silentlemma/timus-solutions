#include <cstdint>
#include <cstdio>
#include <iostream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

const int SIDE = 7;
const int ARM = 2; // the corners cut from the 7 x 7 square are 2 x 2
const string LETTERS = "ABCDEFG";
const int DIRECTIONS = 4;
const int DR[DIRECTIONS] = {0, 1, 0, -1}, DC[DIRECTIONS] = {1, 0, -1, 0};
const int CLASSES = 3; // the residues behind the invariant

struct Move {
    uint64_t from, over, to;
    int i, j;
};

vector<Move> moves;
unordered_set<uint64_t> dead;
vector<pair<int, int>> path;
uint64_t goal;

bool onBoard(int r, int c) {
    return r >= 0 && r < SIDE && c >= 0 && c < SIDE &&
           ((r >= ARM && r < SIDE - ARM) || (c >= ARM && c < SIDE - ARM));
}

bool solve(uint64_t board) {
    if (board == goal)
        return true;
    if (dead.count(board))
        return false;
    for (const Move &m : moves)
        if ((board & m.from) && (board & m.over) && !(board & m.to)) {
            path.push_back({m.i, m.j});
            if (solve(board ^ m.from ^ m.over ^ m.to))
                return true;
            path.pop_back();
        }
    dead.insert(board);
    return false;
}

int main() {
    string target;
    if (!(cin >> target))
        return 0;
    int tc = LETTERS.find(target[0]), tr = target[1] - '1', centre = SIDE / 2;
    // A jump changes the parity of the peg count in each class of r + c
    // (mod 3), and of r - c: so the last peg sits where r and c are both
    // congruent to the centre modulo 3.
    if ((tr - centre) % CLASSES || (tc - centre) % CLASSES || !onBoard(tr, tc)) {
        printf("Impossible\n");
        return 0;
    }
    // The start is symmetric, so an edge target is a quarter turn of the top
    // one: search for the top cell, which the search finds fast, then turn.
    int turns = 0;
    while (!(tr == centre && tc == centre) && !(tr == SIDE - 1 && tc == centre)) {
        int r = SIDE - 1 - tc, c = tr; // a quarter turn back
        tr = r, tc = c;
        turns++;
    }
    vector<pair<int, int>> cells;
    int index[SIDE][SIDE];
    for (int r = 0; r < SIDE; r++)
        for (int c = 0; c < SIDE; c++)
            if (onBoard(r, c)) {
                index[r][c] = cells.size();
                cells.push_back({r, c});
            }
    // every move as (from, over, to) bits
    for (auto [r, c] : cells)
        for (int d = 0; d < DIRECTIONS; d++) {
            int r1 = r + DR[d], c1 = c + DC[d], r2 = r + 2 * DR[d], c2 = c + 2 * DC[d];
            if (onBoard(r1, c1) && onBoard(r2, c2))
                moves.push_back({1ULL << index[r][c], 1ULL << index[r1][c1], 1ULL << index[r2][c2],
                                 index[r][c], index[r2][c2]});
        }
    uint64_t full = (1ULL << cells.size()) - 1;
    uint64_t start = full & ~(1ULL << index[centre][centre]);
    goal = 1ULL << index[tr][tc];
    solve(start);
    auto name = [&](int i) {
        auto [r, c] = cells[i];
        for (int t = 0; t < turns; t++) {
            int nr = c, nc = SIDE - 1 - r; // a quarter turn forward
            r = nr, c = nc;
        }
        return string(1, LETTERS[c]) + char('1' + r);
    };
    for (auto [i, j] : path)
        printf("%s-%s\n", name(i).c_str(), name(j).c_str());
}
