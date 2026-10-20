#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    constexpr int MAX_LENGTH = 1000000000;
    constexpr int INF = MAX_LENGTH + 1;
    std::vector<std::vector<int>> graph(n + 1);
    std::vector<int> first(n + 1), second(n + 1);
    std::vector<int> shortest(n + 1, INF), next_shortest(n + 1, INF);
    auto add = [&](int u, int v, int length) {
        graph[u].push_back(v);
        if (length < shortest[u]) {
            next_shortest[u] = shortest[u];
            second[u] = first[u];
            shortest[u] = length;
            first[u] = v;
        } else if (length < next_shortest[u]) {
            next_shortest[u] = length;
            second[u] = v;
        }
    };
    for (int i = 1; i < n; ++i) {
        int u, v, length;
        std::cin >> u >> v >> length;
        add(u, v, length);
        add(v, u, length);
    }

    std::vector<int> parent(n + 1), order{1};
    order.reserve(n);
    for (int i = 0; i < n; ++i) {
        int v = order[i];
        for (int u : graph[v]) {
            if (u != parent[v]) {
                parent[u] = v;
                order.push_back(u);
            }
        }
    }

    // down[v] is the endpoint after arriving at v from its parent.
    std::vector<int> down(n + 1), up(n + 1);
    for (int i = n - 1; i >= 0; --i) {
        int v = order[i];
        int u = first[v] == parent[v] ? second[v] : first[v];
        down[v] = u == 0 ? v : down[u];
    }
    // up[v] is the endpoint after leaving v for its parent.
    for (int i = 1; i < n; ++i) {
        int v = order[i], p = parent[v];
        int u = first[p] == v ? second[p] : first[p];
        up[v] = u == 0 ? p : (u == parent[p] ? up[p] : down[u]);
    }
    for (int v = 1; v <= n; ++v) {
        if (v != 1) {
            std::cout << ' ';
        }
        std::cout << (first[v] == parent[v] ? up[v] : down[v]);
    }
    std::cout << '\n';
}
