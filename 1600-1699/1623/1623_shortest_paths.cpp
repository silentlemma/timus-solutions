#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int INF = 1000000000;
typedef vector<vector<int>> Matrix;

int n, k, size_;
Matrix road;

pair<int, int> door(const string &s) {
    size_t dot = s.find('.');
    return {stoi(s.substr(0, dot)), stoi(s.substr(dot + 1))};
}

// distances between the doors of the outer house when walking through an
// inner house from door i to door j costs inside[i][j]
Matrix outerDistances(const Matrix &inside) {
    Matrix weight = road;
    for (int h = 1; h <= k; h++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (inside[i][j] < weight[h * n + i][h * n + j])
                    weight[h * n + i][h * n + j] = inside[i][j];
    Matrix result(n, vector<int>(n));
    for (int s = 0; s < n; s++) {
        // Dijkstra on the dense graph, O(size^2)
        vector<int> dist(size_, INF);
        vector<bool> done(size_, false);
        dist[s] = 0;
        for (int step = 0; step < size_; step++) {
            int u = -1;
            for (int v = 0; v < size_; v++)
                if (!done[v] && dist[v] < INF && (u < 0 || dist[v] < dist[u]))
                    u = v;
            if (u < 0)
                break;
            done[u] = true;
            for (int v = 0; v < size_; v++)
                if (weight[u][v] < INF && dist[u] + weight[u][v] < dist[v])
                    dist[v] = dist[u] + weight[u][v];
        }
        for (int j = 0; j < n; j++)
            result[s][j] = dist[j];
    }
    return result;
}

int main() {
    int m;
    if (!(cin >> n >> k >> m))
        return 0;
    size_ = (k + 1) * n; // door d of house h is h * n + d
    road.assign(size_, vector<int>(size_, INF));
    for (int i = 0; i < m; i++) {
        string left, dash, right;
        cin >> left >> dash >> right;
        auto [h1, d1] = door(left);
        auto [h2, d2] = door(right);
        int u = h1 * n + d1, v = h2 * n + d2;
        road[u][v] = road[v][u] = 1;
    }
    int source, sink;
    cin >> source >> sink;
    // Round t allows paths nested t houses deep; the distances only shrink,
    // and once a round changes nothing, no later round will.
    Matrix inside = outerDistances(Matrix(n, vector<int>(n, INF)));
    while (true) {
        Matrix next = outerDistances(inside);
        if (next == inside)
            break;
        inside = next;
    }
    if (inside[source][sink] >= INF)
        printf("no solution\n");
    else
        printf("%d\n", inside[source][sink]);
}
