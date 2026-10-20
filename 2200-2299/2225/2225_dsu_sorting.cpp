#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int find_root(std::vector<int> &parent, int vertex) {
    while (parent[vertex] != vertex) {
        parent[vertex] = parent[parent[vertex]];
        vertex = parent[vertex];
    }
    return vertex;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> height(n), order(n), parent(n), size(n, 0);
    for (int &value : height) {
        std::cin >> value;
    }
    std::iota(order.begin(), order.end(), 0);
    std::iota(parent.begin(), parent.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) { return height[a] > height[b]; });

    long long answer = 0;
    for (int vertex : order) {
        size[vertex] = 1;
        answer += height[vertex];
        for (int neighbor : {vertex - 1, vertex + 1}) {
            if (neighbor < 0 || neighbor >= n || size[neighbor] == 0) {
                continue;
            }
            int a = find_root(parent, vertex);
            int b = find_root(parent, neighbor);
            // Joining two odd runs saves one strike at every remaining level.
            if (size[a] % 2 == 1 && size[b] % 2 == 1) {
                answer -= height[vertex];
            }
            if (size[a] < size[b]) {
                std::swap(a, b);
            }
            parent[b] = a;
            size[a] += size[b];
        }
    }
    std::cout << answer << '\n';
}
