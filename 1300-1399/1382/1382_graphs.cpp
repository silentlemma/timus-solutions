#include <algorithm>
#include <cstdio>
#include <map>
#include <utility>
#include <vector>

const int FIELDS = 3;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // variable i is true when friend i's first statement is the true one,
    // and literal 2 v means v while 2 v + 1 means not v
    std::map<std::pair<int, int>, std::vector<int>> groups; // at most one claim holds
    for (int i = 0; i < n; i++) {
        int a = 0, b = 0, c = 0;
        if (scanf("%d %d %d", &a, &b, &c) != FIELDS)
            return 0;
        groups[{0, i + 1}].push_back(2 * i);
        groups[{1, a}].push_back(2 * i);
        groups[{0, b}].push_back(2 * i + 1);
        groups[{1, c}].push_back(2 * i + 1);
    }
    int count = n;
    std::vector<std::pair<int, int>> clauses; // one of the two literals must hold
    for (auto &g : groups) {
        // at most one: helper s_j means some of the first j members holds
        int prev = -1;
        for (int lit : g.second) {
            int s = count++;
            clauses.push_back({lit ^ 1, 2 * s});
            if (prev >= 0) {
                clauses.push_back({2 * prev + 1, 2 * s});
                clauses.push_back({2 * prev + 1, lit ^ 1});
            }
            prev = s;
        }
    }
    int m = 2 * count;
    std::vector<std::vector<int>> graph(m);
    for (auto &cl : clauses) {
        graph[cl.first ^ 1].push_back(cl.second);
        graph[cl.second ^ 1].push_back(cl.first);
    }
    // Tarjan's components, numbered from the sinks up
    std::vector<int> index(m, -1), low(m, 0), comp(m, -1), stack;
    std::vector<bool> onStack(m, false);
    int counter = 0, comps = 0;
    for (int root = 0; root < m; root++) {
        if (index[root] >= 0)
            continue;
        std::vector<std::pair<int, int>> work(1, {root, 0});
        while (!work.empty()) {
            auto [v, k] = work.back();
            work.pop_back();
            if (k == 0) {
                index[v] = low[v] = counter++;
                stack.push_back(v);
                onStack[v] = true;
            } else {
                low[v] = std::min(low[v], low[graph[v][k - 1]]);
            }
            bool descended = false;
            while (k < (int)graph[v].size()) {
                int u = graph[v][k++];
                if (index[u] < 0) {
                    work.push_back({v, k});
                    work.push_back({u, 0});
                    descended = true;
                    break;
                }
                if (onStack[u])
                    low[v] = std::min(low[v], index[u]);
            }
            if (!descended && low[v] == index[v]) {
                while (true) {
                    int u = stack.back();
                    stack.pop_back();
                    onStack[u] = false;
                    comp[u] = comps;
                    if (u == v)
                        break;
                }
                comps++;
            }
        }
    }
    // a literal holds when its component comes before its negation's
    for (int i = 0; i < n; i++)
        printf("%d%c", comp[2 * i] < comp[2 * i + 1] ? 1 : 2, i + 1 < n ? ' ' : '\n');
    return 0;
}
