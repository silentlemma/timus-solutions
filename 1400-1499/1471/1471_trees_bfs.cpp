#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

const int INPUT_BUFFER = 4096;
// refilling this small buffer keeps memory independent of the input size.
int nextInt() {
    static char buffer[INPUT_BUFFER];
    static int position = 0, size = 0;
    auto read = [&]() -> int {
        if (position == size) {
            size = static_cast<int>(std::fread(buffer, 1, INPUT_BUFFER, stdin));
            position = 0;
            if (size == 0)
                return EOF;
        }
        return buffer[position++];
    };
    int c = read();
    while (c != EOF && c != '-' && (c < '0' || c > '9'))
        c = read();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = read();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value * sign;
}

int main() {
    int n = nextInt();
    std::vector<std::vector<std::pair<int, int>>> edges(n);
    for (int i = 1; i < n; ++i) {
        int u = nextInt(), v = nextInt(), w = nextInt();
        edges[u].push_back({v, w});
        edges[v].push_back({u, w});
    }
    // n <= 50000 and weights <= 1000 keep distance sums below 100 million.
    std::vector<int> parent(n, -1), depth(n), distance(n), size(n, 1), heavy(n, -1), top(n);
    std::vector<int> order{0};
    order.reserve(n);
    for (int i = 0; i < n; ++i) {
        int v = order[i];
        for (auto edge : edges[v])
            if (edge.first != parent[v]) {
                int u = edge.first;
                parent[u] = v;
                depth[u] = depth[v] + 1;
                distance[u] = distance[v] + edge.second;
                order.push_back(u);
            }
    }
    for (int i = n - 1; i > 0; --i) {
        int v = order[i], p = parent[v];
        size[p] += size[v];
        if (heavy[p] < 0 || size[v] > size[heavy[p]])
            heavy[p] = v;
    }
    // every jump across a light edge at least doubles the remaining subtree size.
    for (int v : order)
        if (v != 0)
            top[v] = heavy[parent[v]] == v ? top[parent[v]] : v;
    int m = nextInt();
    for (int i = 0; i < m; ++i) {
        int a = nextInt(), b = nextInt(), answer = distance[a] + distance[b];
        while (top[a] != top[b]) {
            if (depth[top[a]] < depth[top[b]])
                std::swap(a, b);
            a = parent[top[a]];
        }
        int ancestor = depth[a] < depth[b] ? a : b;
        std::printf("%d\n", answer - 2 * distance[ancestor]);
    }
}
