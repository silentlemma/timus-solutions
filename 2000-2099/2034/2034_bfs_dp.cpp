#include <algorithm>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

std::pair<std::vector<int>, std::vector<int>> bfs(const std::vector<std::vector<int>> &neighbors,
                                                  int source) {
    std::vector<int> distance(neighbors.size(), -1), order{source};
    distance[source] = 0;
    for (std::size_t at = 0; at < order.size(); ++at) {
        int vertex = order[at];
        for (int next : neighbors[vertex]) {
            if (distance[next] == -1) {
                distance[next] = distance[vertex] + 1;
                order.push_back(next);
            }
        }
    }
    return {std::move(distance), std::move(order)};
}

int solve(int size, const std::vector<std::pair<int, int>> &edges, int start, int finish,
          int origin) {
    std::vector<std::vector<int>> neighbors(size);
    for (auto edge : edges) {
        neighbors[edge.first].push_back(edge.second);
        neighbors[edge.second].push_back(edge.first);
    }
    auto first = bfs(neighbors, start);
    auto from_origin = bfs(neighbors, origin).first;
    std::vector<int> best(size, -1);
    best[start] = from_origin[start];
    for (int vertex : first.second) {
        for (int next : neighbors[vertex]) {
            if (first.first[next] == first.first[vertex] + 1)
                best[next] = std::max(best[next], std::min(best[vertex], from_origin[next]));
        }
    }
    return best[finish];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size, count;
    if (!(std::cin >> size >> count))
        return 0;
    std::vector<std::pair<int, int>> edges;
    edges.reserve(count);
    for (int i = 0; i < count; ++i) {
        int a, b;
        std::cin >> a >> b;
        edges.emplace_back(a - 1, b - 1);
    }
    int start, finish, origin;
    std::cin >> start >> finish >> origin;
    std::cout << solve(size, edges, start - 1, finish - 1, origin - 1) << '\n';
}
