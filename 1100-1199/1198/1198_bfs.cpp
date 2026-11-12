#include <iostream>
#include <vector>

using Graph = std::vector<std::vector<char>>;

int markReachable(const Graph &edge, int start, std::vector<char> &seen, bool reverse = false) {
    std::vector<int> queue{start};
    seen[start] = true;
    const int n = static_cast<int>(edge.size());
    for (std::size_t head = 0; head < queue.size(); ++head) {
        int from = queue[head];
        for (int to = 0; to < n; ++to) {
            bool adjacent = reverse ? edge[to][from] : edge[from][to];
            if (adjacent && !seen[to]) {
                seen[to] = true;
                queue.push_back(to);
            }
        }
    }
    return static_cast<int>(queue.size());
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;

    Graph edge(n, std::vector<char>(n));
    for (int from = 0; from < n; ++from) {
        int to;
        while (std::cin >> to && to != 0)
            edge[from][to - 1] = true;
    }

    std::vector<char> seen(n);
    int candidate = 0;
    for (int vertex = 0; vertex < n; ++vertex) {
        if (!seen[vertex]) {
            candidate = vertex;
            markReachable(edge, candidate, seen);
        }
    }

    std::vector<char> forward(n), backward(n);
    if (markReachable(edge, candidate, forward) == n) {
        markReachable(edge, candidate, backward, true);
        for (int vertex = 0; vertex < n; ++vertex)
            if (backward[vertex])
                std::cout << vertex + 1 << ' ';
    }
    std::cout << "0\n";
}
