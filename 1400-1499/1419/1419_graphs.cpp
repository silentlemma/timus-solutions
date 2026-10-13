#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

const size_t DEGREE = 3;

struct Frame {
    int v, via;
    size_t k;
};

bool realMap(int w, int h, const vector<string> &lines) {
    vector<vector<pair<int, int>>> adj(w * h);
    int edges = 0;
    for (int r = 0; r < (int)lines.size(); r++)
        for (int c = 0; c < (int)lines[r].size(); c++) {
            char ch = lines[r][c];
            if ((r % 2 == 0 && c % 2 == 0) || ch == ' ')
                continue;
            // the symbol must fit its gap: - between columns, | between rows, \ or / across
            int dr, dc;
            if (r % 2 == 0 && ch == '-')
                dr = 0, dc = 1;
            else if (c % 2 == 0 && ch == '|')
                dr = 1, dc = 0;
            else if (r % 2 == 1 && c % 2 == 1 && (ch == '\\' || ch == '/'))
                dr = 1, dc = ch == '/' ? -1 : 1;
            else
                return false;
            int a = (r - dr) / 2 * w + (c - dc) / 2, b = a + dr * w + dc;
            adj[a].push_back({b, edges});
            adj[b].push_back({a, edges});
            edges++;
        }
    for (auto &v : adj)
        if (v.size() != DEGREE)
            return false;
    // iterative low-link search: a tree edge to v is a bridge if low[v] > tin[parent]
    vector<int> tin(w * h, -1), low(w * h, 0);
    tin[0] = 0;
    int timer = 0;
    vector<Frame> stack = {{0, -1, 0}};
    while (!stack.empty()) {
        Frame &f = stack.back();
        int v = f.v;
        if (f.k < adj[v].size()) {
            auto [u, e] = adj[v][f.k++];
            if (e == f.via)
                continue;
            if (tin[u] < 0) {
                tin[u] = low[u] = ++timer;
                stack.push_back({u, e, 0});
            } else {
                low[v] = min(low[v], tin[u]);
            }
            continue;
        }
        stack.pop_back();
        if (!stack.empty()) {
            int p = stack.back().v;
            low[p] = min(low[p], low[v]);
            if (low[v] > tin[p])
                return false;
        }
    }
    return *min_element(tin.begin(), tin.end()) >= 0;
}

int main() {
    int m, n;
    string line;
    getline(cin, line);
    sscanf(line.c_str(), "%d %d", &m, &n);
    vector<string> picture(n, string(m, ' '));
    for (int r = 0; r < n && getline(cin, line); r++)
        for (int c = 0; c < m && c < (int)line.size(); c++)
            if (line[c] != '\r')
                picture[r][c] = line[c];
    bool ok = realMap((m + 1) / 2, (n + 1) / 2, picture);
    cout << (ok ? "Island world" : "Just a picture") << endl;
}
