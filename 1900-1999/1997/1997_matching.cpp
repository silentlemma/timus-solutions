#include <iostream>
#include <queue>
#include <utility>
#include <vector>

struct Matcher {
    std::vector<std::vector<int>> edges;
    std::vector<int> left, right, distance, cursor;
    int count, shortest;

    explicit Matcher(std::vector<std::vector<int>> graph)
        : edges(std::move(graph)), left(edges.size(), -1), right(edges.size(), -1),
          distance(edges.size()), cursor(edges.size()), count(static_cast<int>(edges.size())),
          shortest(0) {}

    bool layer() {
        std::queue<int> queue;
        shortest = count + 1;
        for (int u = 0; u < count; ++u) {
            distance[u] = left[u] < 0 ? 0 : -1;
            cursor[u] = 0;
            if (left[u] < 0)
                queue.push(u);
        }
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            if (distance[u] >= shortest)
                continue;
            for (int v : edges[u]) {
                int mate = right[v];
                if (mate < 0)
                    shortest = distance[u] + 1;
                else if (distance[mate] < 0) {
                    distance[mate] = distance[u] + 1;
                    queue.push(mate);
                }
            }
        }
        return shortest <= count;
    }

    bool augment(int u) {
        while (cursor[u] < static_cast<int>(edges[u].size())) {
            int v = edges[u][cursor[u]++], mate = right[v];
            if ((mate < 0 && distance[u] + 1 == shortest) ||
                (mate >= 0 && distance[mate] == distance[u] + 1 && augment(mate))) {
                left[u] = v;
                right[v] = u;
                return true;
            }
        }
        distance[u] = -1;
        return false;
    }

    bool perfect() {
        int total = 0;
        while (layer()) {
            for (int u = 0; u < count; ++u)
                if (left[u] < 0 && augment(u))
                    ++total;
        }
        return total == count;
    }
};

std::vector<std::pair<int, int>> solve(int a, int b,
                                       const std::vector<std::pair<int, int>> &records) {
    std::vector<int> entries, exits;
    for (auto record : records)
        (record.second == 0 ? entries : exits).push_back(record.first);
    if (entries.size() != exits.size())
        return {};
    int count = static_cast<int>(entries.size());
    std::vector<std::vector<int>> edges(count);
    for (int u = 0; u < count; ++u)
        for (int v = 0; v < count; ++v) {
            int duration = exits[v] - entries[u];
            if (duration > 0 && (duration <= b || duration >= a))
                edges[u].push_back(v);
        }
    Matcher matcher(std::move(edges));
    if (!matcher.perfect())
        return {};
    std::vector<std::pair<int, int>> answer;
    for (int u = 0; u < count; ++u)
        answer.emplace_back(entries[u], exits[matcher.left[u]]);
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int a, b, n;
    std::cin >> a >> b >> n;
    std::vector<std::pair<int, int>> records(n);
    for (auto &record : records)
        std::cin >> record.first >> record.second;
    auto answer = solve(a, b, records);
    if (answer.empty())
        std::cout << "Liar\n";
    else {
        std::cout << "No reason\n";
        for (auto pair : answer)
            std::cout << pair.first << ' ' << pair.second << '\n';
    }
}
