#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

constexpr int PERCENT_SCALE = 100;
constexpr int PROBABILITY_DIGITS = 12;

struct Route {
    std::vector<int> path;
    double risk;
};

Route safestShortestPath(const std::vector<std::vector<int>> &adjacency, int start, int target) {
    const int count = static_cast<int>(adjacency.size());
    std::array<double, PERCENT_SCALE> costs{};
    for (int probability = 0; probability < PERCENT_SCALE; ++probability) {
        costs[probability] = -std::log1p(-static_cast<double>(probability) / PERCENT_SCALE);
    }
    std::vector<int> distance(count, -1), parent(count, -1), queue;
    std::vector<double> best(count, std::numeric_limits<double>::infinity());
    distance[start] = 0;
    best[start] = 0;
    queue.push_back(start);
    for (std::size_t head = 0; head < queue.size(); ++head) {
        const int city = queue[head];
        if (city == target) {
            break;
        }
        for (int edge : adjacency[city]) {
            const int neighbor = edge / PERCENT_SCALE;
            const int probability = edge % PERCENT_SCALE;
            if (distance[neighbor] < 0) {
                distance[neighbor] = distance[city] + 1;
                queue.push_back(neighbor);
            }
            if (distance[neighbor] == distance[city] + 1) {
                const double candidate = best[city] + costs[probability];
                if (candidate < best[neighbor]) {
                    best[neighbor] = candidate;
                    parent[neighbor] = city;
                }
            }
        }
    }
    std::vector<int> path;
    for (int city = target; city >= 0; city = parent[city]) {
        path.push_back(city);
    }
    std::reverse(path.begin(), path.end());
    return {path, -std::expm1(-best[target])};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count, roads, start, target;
    std::cin >> count >> roads >> start >> target;
    --start;
    --target;
    std::vector<std::vector<int>> adjacency(count);
    for (int index = 0; index < roads; ++index) {
        int first, second, probability;
        std::cin >> first >> second >> probability;
        --first;
        --second;
        adjacency[first].push_back(PERCENT_SCALE * second + probability);
        adjacency[second].push_back(PERCENT_SCALE * first + probability);
    }
    const Route route = safestShortestPath(adjacency, start, target);
    std::cout << route.path.size() << ' ' << std::fixed << std::setprecision(PROBABILITY_DIGITS)
              << route.risk << '\n';
    for (std::size_t index = 0; index < route.path.size(); ++index) {
        if (index != 0) {
            std::cout << ' ';
        }
        std::cout << route.path[index] + 1;
    }
    std::cout << '\n';
    return 0;
}
