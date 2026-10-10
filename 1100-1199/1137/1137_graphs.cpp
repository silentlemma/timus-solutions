#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

// stop numbers are at most this
const int STOPS = 1000;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> adj(STOPS + 1);
    int edges = 0, start = -1;
    for (int r = 0; r < n; r++) {
        int m;
        if (scanf("%d", &m) != 1)
            return 0;
        std::vector<int> stops(m + 1);
        for (auto &s : stops)
            if (scanf("%d", &s) != 1)
                return 0;
        if (start < 0)
            start = stops[0];
        for (int k = 0; k < m; k++)
            adj[stops[k]].push_back(stops[k + 1]);
        edges += m;
    }
    // every old route is a cycle, so each stop is left as often as it is
    // entered; Hierholzer's walk then uses every segment once
    std::vector<size_t> ptr(STOPS + 1, 0);
    std::vector<int> stack = {start}, circuit;
    while (!stack.empty()) {
        int v = stack.back();
        if (ptr[v] < adj[v].size())
            stack.push_back(adj[v][ptr[v]++]);
        else {
            circuit.push_back(v);
            stack.pop_back();
        }
    }
    if ((int)circuit.size() != edges + 1) {
        puts("0");
        return 0;
    }
    std::reverse(circuit.begin(), circuit.end());
    std::string out = std::to_string(edges);
    for (int v : circuit)
        out += " " + std::to_string(v);
    puts(out.c_str());
}
