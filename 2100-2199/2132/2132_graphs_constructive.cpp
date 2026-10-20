#include <iostream>
#include <vector>

namespace {
constexpr int kMaxLabel = 100000;
constexpr int kRootParent = -1;

struct Path {
    int first;
    int center;
    int last;
};
} // namespace

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<std::vector<int>> adjacent(kMaxLabel + 1);
    int largest = 0;
    int first;
    int second;
    while (std::cin >> first >> second) {
        adjacent[first].push_back(second);
        adjacent[second].push_back(first);
        if (first > largest) {
            largest = first;
        }
        if (second > largest) {
            largest = second;
        }
    }

    std::vector<int> parent(largest + 1);
    std::vector<int> rank(largest + 1);
    std::vector<int> order;
    std::vector<int> stack;
    order.reserve(largest);
    stack.reserve(largest);

    for (int root = 1; root <= largest; ++root) {
        if (parent[root] != 0 || adjacent[root].empty()) {
            continue;
        }
        parent[root] = kRootParent;
        stack.push_back(root);
        while (!stack.empty()) {
            const int vertex = stack.back();
            stack.pop_back();
            rank[vertex] = static_cast<int>(order.size());
            order.push_back(vertex);
            for (const int endpoint : adjacent[vertex]) {
                if (parent[endpoint] == 0) {
                    parent[endpoint] = vertex;
                    stack.push_back(endpoint);
                }
            }
        }
    }

    std::vector<bool> used_parent(largest + 1);
    std::vector<Path> answer;
    for (auto position = order.rbegin(); position != order.rend(); ++position) {
        const int vertex = *position;
        int pending = 0;
        for (const int endpoint : adjacent[vertex]) {
            if (endpoint == parent[vertex]) {
                continue;
            }
            if (parent[endpoint] == vertex) {
                if (used_parent[endpoint]) {
                    continue;
                }
            } else if (rank[endpoint] > rank[vertex]) {
                continue;
            }

            if (pending == 0) {
                pending = endpoint;
            } else {
                answer.push_back({pending, vertex, endpoint});
                pending = 0;
            }
        }
        if (pending != 0) {
            if (parent[vertex] == kRootParent) {
                std::cout << kRootParent << '\n';
                return 0;
            }
            answer.push_back({pending, vertex, parent[vertex]});
            used_parent[vertex] = true;
        }
    }

    std::cout << answer.size() << '\n';
    for (const Path &path : answer) {
        std::cout << path.first << ' ' << path.center << ' ' << path.last << '\n';
    }
}
