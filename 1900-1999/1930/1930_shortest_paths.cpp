#include <deque>
#include <iostream>
#include <vector>

int minimumChanges(const std::vector<std::vector<int>> &adjacency, int start, int target) {
    const int stateCount = 2 * static_cast<int>(adjacency.size());
    std::vector<int> distance(stateCount, stateCount);
    std::vector<bool> settled(stateCount, false);
    const int first = 2 * start;
    distance[first] = distance[first + 1] = 0;
    std::deque<int> queue{first, first + 1};
    while (!queue.empty()) {
        const int state = queue.front();
        queue.pop_front();
        if (settled[state]) {
            continue;
        }
        settled[state] = true;
        const int city = state / 2;
        const int gear = state & 1;
        if (city == target) {
            return distance[state];
        }
        for (const int nextState : adjacency[city]) {
            const int cost = (nextState & 1) != gear;
            const int candidate = distance[state] + cost;
            if (candidate < distance[nextState]) {
                distance[nextState] = candidate;
                if (cost == 0) {
                    queue.push_front(nextState);
                } else {
                    queue.push_back(nextState);
                }
            }
        }
    }
    return -1;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count, roads;
    std::cin >> count >> roads;
    std::vector<std::vector<int>> adjacency(count);
    for (int i = 0; i < roads; ++i) {
        int lower, upper;
        std::cin >> lower >> upper;
        --lower;
        --upper;
        adjacency[lower].push_back(2 * upper);
        adjacency[upper].push_back(2 * lower + 1);
    }
    int start, target;
    std::cin >> start >> target;
    std::cout << minimumChanges(adjacency, start - 1, target - 1) << '\n';
    return 0;
}
