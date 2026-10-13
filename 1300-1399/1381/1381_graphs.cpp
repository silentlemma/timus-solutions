#include <cstdio>
#include <vector>

struct Edge {
    int from, to, weight;
};

std::vector<int> reach(const std::vector<std::vector<int>> &links) {
    std::vector<int> seen(links.size(), 0), stack(1, 0);
    seen[0] = 1;
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        for (int u : links[v])
            if (!seen[u]) {
                seen[u] = 1;
                stack.push_back(u);
            }
    }
    return seen;
}

// Bellman-Ford from every node at once: is some cycle negative
bool negativeCycle(int nodes, const std::vector<Edge> &edges, int sign) {
    std::vector<long long> dist(nodes, 0);
    for (int round = 0; round < nodes; round++) {
        bool changed = false;
        for (const Edge &e : edges)
            if (dist[e.from] + sign * e.weight < dist[e.to]) {
                dist[e.to] = dist[e.from] + sign * e.weight;
                changed = true;
            }
        if (!changed)
            return false;
    }
    return true;
}

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    int s = n + 1;
    // rule[j][i][k]: cockroaches next month in a flat with j, i below, k above
    std::vector<std::vector<std::vector<int>>> rule(
        s, std::vector<std::vector<int>>(s, std::vector<int>(s)));
    for (int j = 0; j < s; j++)
        for (int i = 0; i < s; i++)
            for (int k = 0; k < s; k++)
                if (scanf("%d", &rule[j][i][k]) != 1)
                    return 0;
    // a finite floor plan read upwards is a closed walk through the pair (0, 0)
    // of the graph on pairs of neighbours; a step (a, b) -> (b, c) changes the
    // total by rule[b][a][c] - b, so the totals of a walk give the change
    std::vector<std::vector<int>> outOf(s * s), into(s * s);
    std::vector<Edge> all;
    for (int a = 0; a < s; a++)
        for (int b = 0; b < s; b++)
            for (int c = 0; c < s; c++) {
                all.push_back({a * s + b, b * s + c, rule[b][a][c] - b});
                outOf[a * s + b].push_back(b * s + c);
                into[b * s + c].push_back(a * s + b);
            }
    std::vector<int> forward = reach(outOf), backward = reach(into);
    std::vector<Edge> edges;
    for (const Edge &e : all)
        if (forward[e.from] && backward[e.from] && forward[e.to] && backward[e.to])
            edges.push_back(e);
    bool fall = negativeCycle(s * s, edges, 1), rise = negativeCycle(s * s, edges, -1);
    puts(fall ? (rise ? "<>" : "<") : (rise ? ">" : "="));
    return 0;
}
