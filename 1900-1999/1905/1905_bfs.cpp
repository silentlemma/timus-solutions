#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int64_t TIME_BASE = 1000001;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int planets, count;
    std::cin >> planets >> count;
    std::vector<int64_t> origins(count), destinations(count), keys;
    keys.reserve(2 * count + 2);
    for (int i = 0; i < count; ++i) {
        int from, to, leave, enter;
        std::cin >> from >> to >> leave >> enter;
        origins[i] = from * TIME_BASE + leave;
        destinations[i] = to * TIME_BASE + enter;
        keys.push_back(origins[i]);
        keys.push_back(destinations[i]);
    }
    int source_planet, goal_planet, start, deadline;
    std::cin >> source_planet >> goal_planet >> start >> deadline;
    const int64_t source_key = source_planet * TIME_BASE + start;
    const int64_t goal_key = goal_planet * TIME_BASE + deadline;
    keys.push_back(source_key);
    keys.push_back(goal_key);
    std::sort(keys.begin(), keys.end());
    keys.erase(std::unique(keys.begin(), keys.end()), keys.end());
    auto index = [&](int64_t key) {
        return static_cast<int>(std::lower_bound(keys.begin(), keys.end(), key) - keys.begin());
    };
    const int nodes = static_cast<int>(keys.size());
    std::vector<int> head(nodes, -1), arrival(count), following(count);
    for (int i = 0; i < count; ++i) {
        const int from = index(origins[i]);
        arrival[i] = index(destinations[i]);
        following[i] = head[from];
        head[from] = i;
    }
    const int source = index(source_key), goal = index(goal_key);
    std::vector<int> previous(nodes, -1), used_flight(nodes), queue;
    queue.reserve(nodes);
    queue.push_back(source);
    previous[source] = source;
    size_t cursor = 0;
    while (cursor < queue.size() && previous[goal] == -1) {
        const int node = queue[cursor++];
        const int next = node + 1;
        if (next < nodes && keys[node] / TIME_BASE == keys[next] / TIME_BASE &&
            previous[next] == -1) {
            previous[next] = node;
            queue.push_back(next);
        }
        for (int flight = head[node]; flight != -1; flight = following[flight]) {
            const int to = arrival[flight];
            if (previous[to] == -1) {
                previous[to] = node;
                used_flight[to] = flight + 1;
                queue.push_back(to);
            }
        }
    }
    if (previous[goal] == -1) {
        std::cout << "Impossible\n";
        return 0;
    }
    std::vector<int> route;
    for (int node = goal; node != source; node = previous[node]) {
        if (used_flight[node])
            route.push_back(used_flight[node]);
    }
    std::reverse(route.begin(), route.end());
    std::cout << route.size() << '\n';
    for (size_t i = 0; i < route.size(); ++i)
        std::cout << (i ? " " : "") << route[i];
    std::cout << '\n';
}
