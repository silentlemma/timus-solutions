#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int CORNERS = 4; // cells in a group of mirror positions
const int INF = 1 << 29;
const int LETTERS = 26;

// the least total cost of giving each row its own column of a square matrix,
// by the potentials method in O(n^3)
int hungarian(const vector<vector<int>> &cost) {
    int n = cost.size();
    vector<int> u(n + 1, 0), v(n + 1, 0), owner(n + 1, 0), prev(n + 1, 0);
    for (int row = 1; row <= n; row++) {
        owner[0] = row;
        int col0 = 0;
        vector<int> least(n + 1, INF);
        vector<bool> used(n + 1, false);
        while (owner[col0]) {
            used[col0] = true;
            int r = owner[col0], delta = INF, col1 = 0;
            for (int c = 1; c <= n; c++)
                if (!used[c]) {
                    int reduced = cost[r - 1][c - 1] - u[r] - v[c];
                    if (reduced < least[c])
                        least[c] = reduced, prev[c] = col0;
                    if (least[c] < delta)
                        delta = least[c], col1 = c;
                }
            for (int c = 0; c <= n; c++)
                if (used[c])
                    u[owner[c]] += delta, v[c] -= delta;
                else
                    least[c] -= delta;
            col0 = col1;
        }
        while (col0) {
            int col1 = prev[col0];
            owner[col0] = owner[col1];
            col0 = col1;
        }
    }
    return -v[0];
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    for (auto &row : grid)
        cin >> row;
    // every row and column symmetric means the four mirror images of a cell
    // hold one kind of statue; each group then gets one kind
    vector<string> groups;
    for (int i = 0; i < n / 2; i++)
        for (int j = 0; j < m / 2; j++)
            groups.push_back(string() + grid[i][j] + grid[i][m - 1 - j] + grid[n - 1 - i][j] +
                             grid[n - 1 - i][m - 1 - j]);
    // a kind with c statues fills c / 4 groups; one column per such place
    vector<int> count(LETTERS, 0);
    for (auto &row : grid)
        for (char c : row)
            count[c - 'a']++;
    vector<char> slots;
    for (int k = 0; k < LETTERS; k++)
        for (int t = 0; t < count[k] / CORNERS; t++)
            slots.push_back((char)('a' + k));
    // a statue not already in place is carried once, and a cycle of k statues
    // takes k carries, so the answer is the number of statues that change
    vector<vector<int>> cost(groups.size(), vector<int>(slots.size()));
    for (size_t g = 0; g < groups.size(); g++)
        for (size_t s = 0; s < slots.size(); s++)
            cost[g][s] = CORNERS - (int)count_if(groups[g].begin(), groups[g].end(),
                                                 [&](char c) { return c == slots[s]; });
    cout << hungarian(cost) << endl;
}
