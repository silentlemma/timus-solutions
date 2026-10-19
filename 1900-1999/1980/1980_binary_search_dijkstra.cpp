#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

constexpr int SEARCH_STEPS = 60;
constexpr int OUTPUT_DIGITS = 12;
constexpr double SAFETY_MARGIN = 1e-8;

struct Edge {
    int a, b, speed, length;
};

std::pair<double, std::vector<int>> solve(int n, const std::vector<Edge> &edges, double deadline) {
    std::vector<std::vector<std::pair<int, int>>> graph(n);
    int totalLength = 0;
    for (int id = 0; id < static_cast<int>(edges.size()); ++id) {
        const Edge &e = edges[id];
        graph[e.a].emplace_back(e.b, id);
        graph[e.b].emplace_back(e.a, id);
        totalLength += e.length;
    }
    std::vector<int> parent(n);
    auto shortest = [&](double extra) {
        std::vector<double> cost(edges.size());
        for (std::size_t i = 0; i < edges.size(); ++i)
            cost[i] = edges[i].length / (edges[i].speed + extra);
        std::vector<double> distance(n, std::numeric_limits<double>::infinity());
        std::fill(parent.begin(), parent.end(), -1);
        using State = std::pair<double, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> queue;
        distance[0] = 0;
        queue.emplace(0, 0);
        while (!queue.empty()) {
            auto [time, vertex] = queue.top();
            queue.pop();
            if (time != distance[vertex])
                continue;
            if (vertex == n - 1)
                return true;
            for (auto [neighbor, id] : graph[vertex]) {
                double candidate = time + cost[id];
                if (candidate <= deadline && candidate < distance[neighbor]) {
                    distance[neighbor] = candidate;
                    parent[neighbor] = id;
                    queue.emplace(candidate, neighbor);
                }
            }
        }
        return false;
    };
    double low = 0, high = 0;
    if (!shortest(0)) {
        high = totalLength / deadline;
        for (int step = 0; step < SEARCH_STEPS; ++step) {
            double middle = (low + high) / 2;
            if (middle == low || middle == high)
                break;
            if (shortest(middle))
                high = middle;
            else
                low = middle;
        }
        shortest(high);
    }
    double extra = high + SAFETY_MARGIN * std::max(1.0, high);
    std::vector<int> path;
    for (int vertex = n - 1; vertex != 0;) {
        int id = parent[vertex];
        path.push_back(id + 1);
        vertex = edges[id].a ^ edges[id].b ^ vertex;
    }
    std::reverse(path.begin(), path.end());
    return {extra, path};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m;
    if (!(std::cin >> n >> m))
        return 0;
    std::vector<Edge> edges(m);
    for (Edge &e : edges) {
        std::cin >> e.a >> e.b >> e.speed >> e.length;
        --e.a;
        --e.b;
    }
    double deadline;
    std::cin >> deadline;
    auto [extra, path] = solve(n, edges, deadline);
    std::cout << std::fixed << std::setprecision(OUTPUT_DIGITS) << extra << ' ' << path.size()
              << '\n';
    for (std::size_t i = 0; i < path.size(); ++i) {
        if (i)
            std::cout << ' ';
        std::cout << path[i];
    }
    std::cout << '\n';
}
