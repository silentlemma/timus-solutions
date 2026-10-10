#include <algorithm>
#include <cstdio>
#include <numeric>
#include <string>
#include <vector>

// a connection is two hubs and a length
const int FIELDS = 3;

struct Edge {
    int a, b, length;
};

std::vector<int> parent;

int find(int v) {
    while (parent[v] != v)
        v = parent[v] = parent[parent[v]];
    return v;
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<Edge> edges(m);
    for (auto &e : edges)
        if (scanf("%d %d %d", &e.a, &e.b, &e.length) != FIELDS)
            return 0;
    std::stable_sort(edges.begin(), edges.end(),
                     [](const Edge &x, const Edge &y) { return x.length < y.length; });
    parent.resize(n + 1);
    std::iota(parent.begin(), parent.end(), 0);
    // Kruskal's tree: its longest cable is the smallest possible longest cable
    // of any plan that connects every hub
    std::vector<Edge> chosen;
    for (const Edge &e : edges) {
        int ra = find(e.a), rb = find(e.b);
        if (ra != rb) {
            parent[ra] = rb;
            chosen.push_back(e);
        }
    }
    std::string out =
        std::to_string(chosen.back().length) + "\n" + std::to_string(chosen.size()) + "\n";
    for (const Edge &e : chosen)
        out += std::to_string(e.a) + " " + std::to_string(e.b) + "\n";
    fputs(out.c_str(), stdout);
}
