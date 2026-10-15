#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

typedef std::vector<std::vector<int>> Graph;

std::vector<bool> reach(int start, const Graph& adj) {
    std::vector<bool> seen(adj.size(), false);
    std::vector<int> stack = {start};
    seen[start] = true;
    while (!stack.empty()) {
        int v = stack.back();
        stack.pop_back();
        for (int u : adj[v]) {
            if (!seen[u]) {
                seen[u] = true;
                stack.push_back(u);
            }
        }
    }
    return seen;
}

int main() {
    int n, m, s, t;
    scanf("%d %d %d %d", &n, &m, &s, &t);
    s--;
    t--;
    std::vector<std::pair<int, int>> edges(m);
    Graph adj(n), radj(n);
    for (auto& [a, b] : edges) {
        scanf("%d %d", &a, &b);
        a--;
        b--;
        adj[a].push_back(b);
        radj[b].push_back(a);
    }
    // only vertices on some path from s to t matter; they form whole
    // strongly connected components
    std::vector<bool> fromS = reach(s, adj);
    if (!fromS[t]) {
        printf("0\n");
        return 0;
    }
    std::vector<bool> toT = reach(t, radj), alive(n);
    for (int v = 0; v < n; v++) {
        alive[v] = fromS[v] && toT[v];
    }
    // Kosaraju: finishing order on the graph, then the reversed graph in
    // reverse finishing order numbers the components in topological order
    std::vector<int> order;
    std::vector<bool> done(n, false);
    for (int root = 0; root < n; root++) {
        if (!alive[root] || done[root]) {
            continue;
        }
        done[root] = true;
        std::vector<std::pair<int, size_t>> stack = {{root, 0}};
        while (!stack.empty()) {
            auto& [v, i] = stack.back();
            if (i < adj[v].size()) {
                int u = adj[v][i++];
                if (alive[u] && !done[u]) {
                    done[u] = true;
                    stack.push_back({u, 0});
                }
            } else {
                order.push_back(v);
                stack.pop_back();
            }
        }
    }
    std::vector<int> comp(n, -1);
    int count = 0;
    for (auto it = order.rbegin(); it != order.rend(); ++it) {
        if (comp[*it] >= 0) {
            continue;
        }
        comp[*it] = count;
        std::vector<int> stack = {*it};
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            for (int u : radj[v]) {
                if (alive[u] && comp[u] < 0) {
                    comp[u] = count;
                    stack.push_back(u);
                }
            }
        }
        count++;
    }
    std::vector<int> size(count, 0), inside(count, 0);
    Graph out(count);
    for (int v = 0; v < n; v++) {
        if (alive[v]) {
            size[comp[v]]++;
        }
    }
    for (auto [a, b] : edges) {
        if (alive[a] && alive[b]) {
            if (comp[a] == comp[b]) {
                inside[comp[a]]++;
            } else {
                out[comp[a]].push_back(comp[b]);
            }
        }
    }
    // a component with more arcs than vertices holds two cycles, and paths grow
    // exponentially; otherwise each cyclic component is one simple cycle, and
    // paths through c of them number about N^(c - 1)
    for (int c = 0; c < count; c++) {
        if (inside[c] > size[c]) {
            printf("-1\n");
            return 0;
        }
    }
    // best[c]: the most cycles on a path from s into component c; arcs go
    // from lower to higher numbers, so one pass in order settles it
    std::vector<int> best(count, 0);
    for (int c = 0; c < count; c++) {
        best[c] += inside[c] == size[c] ? 1 : 0;
        for (int d : out[c]) {
            best[d] = std::max(best[d], best[c]);
        }
    }
    printf("%d\n", std::max(0, best[comp[t]] - 1));
}
