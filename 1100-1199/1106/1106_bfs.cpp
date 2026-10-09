#include <cstdio>
#include <queue>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> adj(n + 1);
    for (int v = 1; v <= n; v++)
        for (int u; scanf("%d", &u) == 1 && u != 0;)
            adj[v].push_back(u);
    // colour a BFS tree of every component by depth parity: each member has a
    // tree neighbour, its parent or a child, in the other team
    std::vector<int> side(n + 1, -1);
    for (int root = 1; root <= n; root++) {
        if (side[root] >= 0)
            continue;
        side[root] = 0;
        std::queue<int> queue;
        queue.push(root);
        while (!queue.empty()) {
            int v = queue.front();
            queue.pop();
            for (int u : adj[v])
                if (side[u] < 0) {
                    side[u] = 1 - side[v];
                    queue.push(u);
                }
        }
    }
    std::vector<int> team;
    for (int v = 1; v <= n; v++)
        if (side[v] == 0)
            team.push_back(v);
    printf("%d\n", (int)team.size());
    for (size_t i = 0; i < team.size(); i++)
        printf(i ? " %d" : "%d", team[i]);
    printf("\n");
}
