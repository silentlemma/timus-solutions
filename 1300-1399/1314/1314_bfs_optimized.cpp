#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int lines;
    if (std::scanf("%d", &lines) != 1)
        return 0;
    std::vector<int> stations;
    std::vector<std::pair<int, int>> edges;
    while (lines--) {
        int length, previous;
        if (std::scanf("%d%d", &length, &previous) != 2)
            return 0;
        stations.push_back(previous);
        for (int i = 1; i < length; ++i) {
            int station;
            if (std::scanf("%d", &station) != 1)
                return 0;
            edges.emplace_back(previous, station);
            stations.push_back(station);
            previous = station;
        }
    }
    std::sort(stations.begin(), stations.end());
    stations.erase(std::unique(stations.begin(), stations.end()), stations.end());
    const int size = static_cast<int>(stations.size());
    const auto index = [&](int station) {
        auto it = std::lower_bound(stations.begin(), stations.end(), station);
        return it != stations.end() && *it == station ? static_cast<int>(it - stations.begin())
                                                      : -1;
    };

    std::vector<int> offsets(size + 1);
    for (auto &[a, b] : edges) {
        a = index(a);
        b = index(b);
        ++offsets[a + 1];
        ++offsets[b + 1];
    }
    for (int i = 1; i <= size; ++i)
        offsets[i] += offsets[i - 1];
    std::vector<int> neighbors(offsets.back());
    auto fill = offsets;
    for (auto [a, b] : edges) {
        neighbors[fill[a]++] = b;
        neighbors[fill[b]++] = a;
    }

    int count, station;
    if (std::scanf("%d%d", &count, &station) != 2)
        return 0;
    const int start = index(station);
    if (start < 0)
        return 0;
    int last = start;
    for (int i = 1; i < count; ++i) {
        if (std::scanf("%d", &station) != 1)
            return 0;
        const int next = index(station);
        const auto begin = neighbors.begin() + offsets[last];
        const auto end = neighbors.begin() + offsets[last + 1];
        if (std::find(begin, end, next) == end)
            return 0;
        last = next;
    }

    std::vector<int> distance(size, -1), queue{start};
    distance[start] = 0;
    for (size_t i = 0; i < queue.size(); ++i) {
        const int a = queue[i];
        for (int j = offsets[a]; j < offsets[a + 1]; ++j) {
            const int b = neighbors[j];
            if (distance[b] < 0) {
                distance[b] = distance[a] + 1;
                queue.push_back(b);
            }
        }
    }
    if (distance[last] != count - 1)
        return 0;

    // A shortest continuation must move exactly one layer forward at every stop.
    std::vector<bool> possible(size);
    possible[last] = true;
    for (int a : queue) {
        if (!possible[a])
            continue;
        for (int j = offsets[a]; j < offsets[a + 1]; ++j) {
            const int b = neighbors[j];
            if (distance[b] == distance[a] + 1)
                possible[b] = true;
        }
    }
    for (int i = 0; i < size; ++i) {
        if (possible[i])
            std::printf("%d\n", stations[i]);
    }
}
