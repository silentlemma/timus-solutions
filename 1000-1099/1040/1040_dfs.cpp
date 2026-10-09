#include <cstdio>
#include <utility>
#include <vector>

std::vector<std::vector<std::pair<int, int>>> adj;
std::vector<int> number;
std::vector<bool> visited;
int counter = 0;

// numbers the flights in the order the search meets them; the first flight
// met at a new airport right after its entry flight k gets k + 1
void dfs(int v) {
    visited[v] = true;
    for (auto [w, e] : adj[v])
        if (number[e] == 0) {
            number[e] = ++counter;
            if (!visited[w])
                dfs(w);
        }
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    adj.resize(n + 1);
    number.assign(m, 0);
    visited.assign(n + 1, false);
    for (int e = 0; e < m; e++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        adj[a].push_back({b, e});
        adj[b].push_back({a, e});
    }
    dfs(1);
    printf("YES\n");
    for (int e = 0; e < m; e++)
        printf("%d%c", number[e], e + 1 < m ? ' ' : '\n');
}
