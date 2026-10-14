#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

const int SIDE = 4, CELLS = SIDE * SIDE;
const int LETTERS = 26;

string grid, word;
vector<int> nearCells[CELLS];
unordered_set<int> dead; // (visited cells, last cell) that cannot finish the word

// cell holds word[i - 1]; mask is every cell used so far
bool walk(int cell, int mask, size_t i) {
    if (i == word.size())
        return true;
    int key = mask * CELLS + cell;
    if (dead.count(key))
        return false;
    for (int next : nearCells[cell])
        if (!(mask >> next & 1) && grid[next] == word[i] && walk(next, mask | 1 << next, i + 1))
            return true;
    dead.insert(key);
    return false;
}

bool found() {
    int have[LETTERS] = {}, need[LETTERS] = {};
    for (char c : grid)
        have[c - 'a']++;
    for (char c : word)
        if (++need[c - 'a'] > have[c - 'a'])
            return false;
    dead.clear();
    for (int c = 0; c < CELLS; c++)
        if (grid[c] == word[0] && walk(c, 1 << c, 1))
            return true;
    return false;
}

int main() {
    for (int r = 0; r < SIDE; r++) {
        string row;
        cin >> row;
        grid += row;
    }
    for (int c = 0; c < CELLS; c++) {
        int r = c / SIDE, col = c % SIDE;
        if (r > 0)
            nearCells[c].push_back(c - SIDE);
        if (r < SIDE - 1)
            nearCells[c].push_back(c + SIDE);
        if (col > 0)
            nearCells[c].push_back(c - 1);
        if (col < SIDE - 1)
            nearCells[c].push_back(c + 1);
    }
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> word;
        cout << word << ": " << (found() ? "YES" : "NO") << "\n";
    }
}
