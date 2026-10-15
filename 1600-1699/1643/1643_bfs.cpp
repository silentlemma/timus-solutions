#include <algorithm>
#include <cstdio>
#include <deque>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int INF = 1 << 29;
const int LETTERS = 26;
const string MARKS = "$!*";  // the two armies and the fortress

int n, m;
vector<string> grid;
vector<vector<int>> gates[LETTERS];

bool isGate(char ch) {
    return ch >= 'A' && ch <= 'Z';
}

// days to every district; teleports are free, so 0-1 BFS
vector<vector<int>> bfs(int sr, int sc, int ar, int ac) {
    vector<vector<int>> dist(n, vector<int>(m, INF));
    vector<bool> used(LETTERS);  // teleport letters already spread
    deque<pair<int, int>> queue = {{sr, sc}};
    dist[sr][sc] = 0;
    while (!queue.empty()) {
        auto [r, c] = queue.front();
        queue.pop_front();
        int d = dist[r][c];
        char ch = grid[r][c];
        if (isGate(ch) && !used[ch - 'A']) {
            used[ch - 'A'] = true;
            for (const vector<int> &g : gates[ch - 'A'])
                if (dist[g[0]][g[1]] > d) {
                    dist[g[0]][g[1]] = d;
                    queue.push_front({g[0], g[1]});
                }
        }
        for (int dr = -1; dr <= 1; dr++)
            for (int dc = -1; dc <= 1; dc++) {
                int nr = r + dr, nc = c + dc;
                if ((!dr && !dc) || nr < 0 || nr >= n || nc < 0 || nc >= m)
                    continue;
                if (grid[nr][nc] == '#' || (nr == ar && nc == ac))
                    continue;
                if (dist[nr][nc] > d + 1) {
                    dist[nr][nc] = d + 1;
                    queue.push_back({nr, nc});
                }
            }
    }
    return dist;
}

int main() {
    if (!(cin >> n >> m))
        return 0;
    grid.resize(n);
    vector<vector<int>> marks(MARKS.size(), vector<int>(2));
    for (int r = 0; r < n; r++) {
        cin >> grid[r];
        for (int c = 0; c < m; c++) {
            char ch = grid[r][c];
            if (isGate(ch))
                gates[ch - 'A'].push_back({r, c});
            size_t k = MARKS.find(ch);
            if (k != string::npos) {
                marks[k][0] = r;
                marks[k][1] = c;
            }
        }
    }
    int fr = marks[2][0], fc = marks[2][1];
    auto first = bfs(marks[0][0], marks[0][1], fr, fc);
    auto second = bfs(marks[1][0], marks[1][1], fr, fc);
    auto attack = bfs(fr, fc, -1, -1);  // moves are symmetric, so this is the way back
    // the earlier army waits at the meeting place, then both march together
    int best = INF;
    for (int r = 0; r < n; r++)
        for (int c = 0; c < m; c++)
            if (r != fr || c != fc)
                best = min(best, max(first[r][c], second[r][c]) + attack[r][c]);
    if (best >= INF)
        puts("Impossible");
    else
        printf("%d\n", best);
}
