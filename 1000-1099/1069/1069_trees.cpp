#include <algorithm>
#include <cstdio>
#include <functional>
#include <queue>
#include <string>
#include <vector>

int main() {
    std::vector<int> code;
    int v;
    while (scanf("%d", &v) == 1)
        code.push_back(v);
    int n = code.size() + 1;
    // a vertex stays until all its neighbours but one are removed, and each
    // removed neighbour writes the vertex once
    std::vector<int> deg(n + 1, 1);
    for (int c : code)
        deg[c]++;
    std::priority_queue<int, std::vector<int>, std::greater<int>> leaves;
    for (int u = 1; u <= n; u++)
        if (deg[u] == 1)
            leaves.push(u);
    std::vector<std::vector<int>> adj(n + 1);
    for (int c : code) {
        int leaf = leaves.top();
        leaves.pop();
        adj[leaf].push_back(c);
        adj[c].push_back(leaf);
        if (--deg[c] == 1)
            leaves.push(c);
    }
    std::string out;
    for (int u = 1; u <= n; u++) {
        std::sort(adj[u].begin(), adj[u].end());
        out += std::to_string(u) + ":";
        for (int w : adj[u])
            out += " " + std::to_string(w);
        out += '\n';
    }
    fputs(out.c_str(), stdout);
}
