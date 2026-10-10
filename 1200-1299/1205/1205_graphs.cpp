#include <cmath>
#include <cstdio>
#include <vector>

int main() {
    double walk, metro;
    int n;
    scanf("%lf %lf %d", &walk, &metro, &n);
    int total = n + 2, start = n, goal = n + 1;
    std::vector<double> x(total), y(total);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf", &x[i], &y[i]);
    }
    std::vector<std::vector<bool>> linked(total, std::vector<bool>(total, false));
    int a, b;
    while (scanf("%d %d", &a, &b) == 2 && (a != 0 || b != 0)) {
        linked[a - 1][b - 1] = linked[b - 1][a - 1] = true;
    }
    scanf("%lf %lf %lf %lf", &x[start], &y[start], &x[goal], &y[goal]);
    // nodes: the stations, then A and B; the subway is never slower than
    // walking, so a linked pair always goes by train
    std::vector<double> dist(total, INFINITY);
    std::vector<int> prev(total, -1);
    std::vector<bool> done(total, false);
    dist[start] = 0;
    for (int step = 0; step < total; step++) {
        int u = -1;
        for (int v = 0; v < total; v++) {
            if (!done[v] && (u < 0 || dist[v] < dist[u])) {
                u = v;
            }
        }
        done[u] = true;
        for (int v = 0; v < total; v++) {
            if (!done[v]) {
                double d = std::hypot(x[v] - x[u], y[v] - y[u]) / (linked[u][v] ? metro : walk);
                if (dist[u] + d < dist[v]) {
                    dist[v] = dist[u] + d;
                    prev[v] = u;
                }
            }
        }
    }
    std::vector<int> path;
    for (int v = prev[goal]; v != start; v = prev[v]) {
        path.push_back(v + 1);
    }
    printf("%.10f\n%d", dist[goal], (int)path.size());
    for (int i = (int)path.size() - 1; i >= 0; i--) {
        printf(" %d", path[i]);
    }
    printf("\n");
}
