#include <cstdio>
#include <vector>

const int INF = 1 << 30;
const int END_OF_INPUT = -1;

int main() {
    int n, m;
    while (scanf("%d", &n) == 1 && n != END_OF_INPUT) {
        scanf("%d", &m);
        // edge: the lightest direct road between two vertices
        std::vector<std::vector<int>> edge(n, std::vector<int>(n, INF)), dist, next(n);
        for (int i = 0; i < n; i++) {
            edge[i][i] = 0;
            for (int j = 0; j < n; j++)
                next[i].push_back(j);
        }
        for (int e = 0; e < m; e++) {
            int a, b, l;
            scanf("%d %d %d", &a, &b, &l);
            a--, b--;
            if (l < edge[a][b])
                edge[a][b] = edge[b][a] = l;
        }
        dist = edge;

        // Floyd-Warshall; before vertex k becomes an intermediate, dist[i][j]
        // uses only vertices below k, so i..j plus j-k-i is a simple cycle.
        int best = INF;
        std::vector<int> cycle;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < k; i++) {
                if (edge[i][k] == INF)
                    continue;
                for (int j = i + 1; j < k; j++) {
                    if (edge[k][j] == INF || dist[i][j] == INF)
                        continue;
                    int c = dist[i][j] + edge[i][k] + edge[k][j];
                    if (c < best) {
                        best = c;
                        cycle.clear();
                        for (int v = i; v != j; v = next[v][j])
                            cycle.push_back(v);
                        cycle.push_back(j);
                        cycle.push_back(k);
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                if (dist[i][k] == INF)
                    continue;
                for (int j = 0; j < n; j++) {
                    int d = dist[i][k] + dist[k][j];
                    if (d < dist[i][j]) {
                        dist[i][j] = d;
                        next[i][j] = next[i][k];
                    }
                }
            }
        }
        if (best == INF) {
            puts("No solution.");
            continue;
        }
        for (size_t i = 0; i < cycle.size(); i++)
            printf("%d%c", cycle[i] + 1, i + 1 < cycle.size() ? ' ' : '\n');
    }
    return 0;
}
